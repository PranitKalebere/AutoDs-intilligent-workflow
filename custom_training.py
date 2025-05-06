import numpy as np
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

def train_custom_model(problem_type, model_name, params, X_train, X_test, y_train, y_test):
    model = None

    if problem_type == 'classification':
        if model_name == 'logistic_regression':
            model = LogisticRegression(**params)
        elif model_name == 'random_forest':
            model = RandomForestClassifier(**params)
        elif model_name == 'neural_network':
            model = Sequential([
                Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
                Dense(32, activation='relu'),
                Dense(len(np.unique(y_train)), activation='softmax')
            ])
            model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
            model.fit(X_train, y_train, epochs=params['epochs'], batch_size=params['batch_size'], verbose=0)
            score = model.evaluate(X_test, y_test, verbose=0)
            return {'accuracy': score[1]}  # Return accuracy

    elif problem_type == 'regression':
        if model_name == 'linear_regression':
            model = LinearRegression()
        elif model_name == 'random_forest':
            model = RandomForestRegressor(**params)
        elif model_name == 'neural_network':
            model = Sequential([
                Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
                Dense(32, activation='relu'),
                Dense(1)
            ])
            model.compile(optimizer=Adam(), loss='mse')
            model.fit(X_train, y_train, epochs=params['epochs'], batch_size=params['batch_size'], verbose=0)
            predictions = model.predict(X_test).flatten()
            return {'mse': mean_squared_error(y_test, predictions)}

    elif problem_type == 'unsupervised':
        if model_name == 'kmeans':
            model = KMeans(**params)
            predictions = model.fit_predict(X_test)
            return {'silhouette_score': silhouette_score(X_test, predictions)}

    if model:
        model.fit(X_train, y_train)
        if problem_type == 'classification':
            predictions = model.predict(X_test)
            return {'accuracy': accuracy_score(y_test, predictions)}
        elif problem_type == 'regression':
            predictions = model.predict(X_test)
            return {'mse': mean_squared_error(y_test, predictions)}
    
    raise ValueError("Invalid combination or parameters.")
