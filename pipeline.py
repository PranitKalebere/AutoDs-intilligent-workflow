import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, mean_squared_error, silhouette_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pickle
import spacy
import re
import os

class AutoMLPipeline:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.models = {}
        self.problem_type = None
        self.target_column = None
        self.feature_columns = None
        
    def analyze_problem_statement(self, statement):
        doc = self.nlp(statement.lower())
        
        supervised_keywords = ['predict', 'classification', 'regression', 'forecast']
        unsupervised_keywords = ['cluster', 'group', 'segment', 'pattern']
        reinforcement_keywords = ['reward', 'action', 'agent', 'environment', 'policy']
        
        supervised_count = sum(1 for word in doc if any(keyword in word.text for keyword in supervised_keywords))
        unsupervised_count = sum(1 for word in doc if any(keyword in word.text for keyword in unsupervised_keywords))
        reinforcement_count = sum(1 for word in doc if any(keyword in word.text for keyword in reinforcement_keywords))
        
        if supervised_count > max(unsupervised_count, reinforcement_count):
            if any(word in statement.lower() for word in ['classify', 'category', 'class']):
                return 'classification'
            else:
                return 'regression'
        elif unsupervised_count > max(supervised_count, reinforcement_count):
            return 'unsupervised'
        else:
            return 'reinforcement'

    def identify_features(self, df, problem_statement):
        doc = self.nlp(problem_statement.lower())

        # Step 1: Try extracting target variable from the problem statement
        potential_targets = []
        for token in doc:
            if token.dep_ in ['dobj', 'pobj', 'attr', 'nsubj'] and token.text in df.columns:
                potential_targets.append(token.text)

        # Step 2: Use extracted target if found, otherwise apply heuristics
        if potential_targets:
            self.target_column = potential_targets[0]
        else:
            # Heuristic 1: If a column contains keywords like 'target', 'label', 'price', 'score', 'class'
            possible_target_columns = [col for col in df.columns if any(keyword in col.lower() 
                                                                        for keyword in ['target', 'label', 'price', 'score', 'class'])]
            if possible_target_columns:
                self.target_column = possible_target_columns[0]
            else:
                # Heuristic 2: If classification, choose column with few unique values
                if self.problem_type == 'classification':
                    self.target_column = df.nunique().idxmin()
                else:
                    # Heuristic 3: If regression, choose a numerical column with higher variance
                    num_columns = df.select_dtypes(include=['number']).columns
                    self.target_column = df[num_columns].var().idxmax() if not num_columns.empty else df.columns[-1]

        # Step 3: Set feature columns
        self.feature_columns = [col for col in df.columns if col != self.target_column]

        return self.target_column, self.feature_columns

    def preprocess_data(self, df):
        df = df.fillna(df.mean() if self.problem_type != 'classification' else df.mode().iloc[0])
        
        for column in df.columns:
            if df[column].dtype == 'object':
                le = LabelEncoder()
                df[column] = le.fit_transform(df[column].astype(str))
        
        scaler = StandardScaler()
        df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)  
        
        return df_scaled

    def train_models(self, problem_type, X_train, X_test, y_train, y_test):
        self.models = {}

        if problem_type == 'classification':
            self.models = {
                'logistic_regression': LogisticRegression(),
                'random_forest': RandomForestClassifier()
            }
            nn_model = Sequential([
                Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
                Dense(32, activation='relu'),
                Dense(len(np.unique(y_train)), activation='softmax')
            ])
            nn_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        elif problem_type == 'regression':
            self.models = {
                'linear_regression': LinearRegression(),
                'random_forest': RandomForestRegressor()
            }
            nn_model = Sequential([
                Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
                Dense(32, activation='relu'),
                Dense(1)
            ])
            nn_model.compile(optimizer='adam', loss='mse')

        elif problem_type == 'unsupervised':
            self.models = {
                'kmeans': KMeans(n_clusters=3)
            }

        results = {}
        for name, model in self.models.items():
            model.fit(X_train, y_train)
            if problem_type == 'classification':
                y_pred = model.predict(X_test)
                results[name] = accuracy_score(y_test, y_pred)
            elif problem_type == 'regression':
                y_pred = model.predict(X_test)
                results[name] = mean_squared_error(y_test, y_pred)
            else:
                predictions = model.predict(X_test)
                results[name] = silhouette_score(X_test, predictions)

        if problem_type in ['classification', 'regression']:
            nn_model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0)
            self.models['neural_network'] = nn_model
            if problem_type == 'classification':
                y_pred = nn_model.predict(X_test).argmax(axis=1)
                results['neural_network'] = accuracy_score(y_test, y_pred)
            else:
                y_pred = nn_model.predict(X_test).flatten()
                results['neural_network'] = mean_squared_error(y_test, y_pred)

        # Return both trained models and their evaluation results
        return self.models, results

    def save_models(self, models ,output_dir='saved_models'):
        os.makedirs(output_dir, exist_ok=True)
        
        for name, model in models.items():
            if 'neural_network' in name:
                model.save(f'{output_dir}/{name}.h5')
            else:
                with open(f'{output_dir}/{name}.pkl', 'wb') as f:
                    pickle.dump(model, f)

    def run_pipeline(self, dataset_path, problem_statement):
        df = pd.read_csv(dataset_path)
        
        self.problem_type = self.analyze_problem_statement(problem_statement)
        print(f"Detected problem type: {self.problem_type}")
        
        target_col, feature_cols = self.identify_features(df, problem_statement)
        print(f"Target column: {target_col}")
        print(f"Feature columns: {feature_cols}")
        
        df_processed = self.preprocess_data(df)
    
        X = df_processed[feature_cols]
        y = df_processed[target_col]       

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        results = self.train_models(X_train, X_test, y_train, y_test)

        self.save_models()
        
        return results

if __name__=="__main__":
    problem_statement = "Predict the house prices based on various features like size, location, and number of rooms"
    dataset_path = "house_prices.csv"  # Replace with your dataset path

    pipeline = AutoMLPipeline()
    results = pipeline.run_pipeline(dataset_path, problem_statement)
    print("\nModel Performance:")
    for model, score in results.items():
        print(f"{model}: {score:.5f}")