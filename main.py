from dashboard import Ui_AutoDs_Intelligent
import sys,os
from PySide6.QtWidgets import (QWidget,QHBoxLayout, QApplication, QMainWindow, QPushButton, QTableWidgetItem)
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QMessageBox)
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QMessageBox,QScrollArea,QTableWidget,QComboBox
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import (
    QApplication, QFrame, QFileDialog, QVBoxLayout, QLabel, QListWidget
)
from PySide6.QtCore import Qt
import pandas as pd
import os
from PySide6.QtGui import QPixmap
import seaborn as sns
import threading
import matplotlib.pyplot as plt
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

from PySide6.QtCore import QObject, Signal, Slot
from sklearn.model_selection import train_test_split
from custom_training import train_custom_model

MODEL_PARAMS = {
    'classification': {
        'logistic_regression': {
            'C': float,
            'max_iter': int
        },
        'random_forest': {
            'n_estimators': int,
            'max_depth': int
        },
        'neural_network': {
            'epochs': int,
            'batch_size': int
        }
    },
    'regression': {
        'linear_regression': {},  # No hyperparameters to tune
        'random_forest': {
            'n_estimators': int,
            'max_depth': int
        },
        'neural_network': {
            'epochs': int,
            'batch_size': int
        }
    },
    'unsupervised': {
        'kmeans': {
            'n_clusters': int,
            'max_iter': int
        }
    }
}

DEFAULT_MODEL_PARAMS = {
    'logistic_regression': {
        'C': 1.0,
        'max_iter': 100,
        'solver': 'lbfgs'
    },
    'random_forest_classifier': {
        'n_estimators': 100,
        'max_depth': None,
        'criterion': 'gini'
    },
    'linear_regression': {
        'fit_intercept': True,
        'copy_X': True
    },
    'random_forest_regressor': {
        'n_estimators': 100,
        'max_depth': None,
        'criterion': 'squared_error'
    },
    'kmeans': {
        'n_clusters': 8,
        'max_iter': 300,
        'init': 'k-means++'
    },
    'neural_network': {
        'epochs': 10,
        'batch_size': 32,
        'optimizer': 'adam',
        'loss': 'auto'
    }
}



class Worker(QObject):
    finished = Signal(dict, dict)
    # output = Signal(dict,dict,dict,dict)
    error = Signal(str)

    def __init__(self, df_processed, feature_cols, target_col, problem_type, pipeliner):
        super().__init__()
        self.df_processed = df_processed
        self.feature_cols = feature_cols
        self.target_col = target_col
        self.problem_type = problem_type
        self.pipeliner = pipeliner

    def run(self):
        try:
            X = self.df_processed[self.feature_cols]
            y = self.df_processed[self.target_col]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            trained_models, results = self.pipeliner.train_models(self.problem_type, X_train, X_test, y_train, y_test)
            self.finished.emit(trained_models, results)
            # self.output.emit(X_train, X_test, y_train, y_test)
        except Exception as e:
            self.error.emit(str(e))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AutoDs_Intelligent()
        self.ui.setupUi(self)    
        self.upload_dataset_page()   
        # self.main_page() 

        self.ui.label_7.setVisible(False)
        self.ui.label_8.setVisible(False)
        self.ui.label_9.setVisible(False)
        self.ui.label_10.setVisible(False)
        self.ui.goto_dashboard.setVisible(False)
        self.ui.goto_dashboard.clicked.connect(self.main_page)
        self.ui.data_info_button.clicked.connect(self.data_info)
        self.ui.visualisation_button.clicked.connect(self.visualisation_page)
        self.ui.model_training_button.clicked.connect(self.model_training_page)
        self.ui.load_data_button.clicked.connect(self.upload_dataset_page)
        self.training_results = None
        from pipeline import AutoMLPipeline
        self.pipeliner = AutoMLPipeline()
        # self.df = pd.read_csv("house_prices.csv")

    def main_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_page)
        self.ui.data_info_button.setChecked(True)
        self.data_info()

    ##### Upload Data Start with Pipeline ###
    def upload_dataset_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.upload_page)
        self.upload_frame = self.ui.upload_data
        self.upload_frame.setAcceptDrops(True)
        self.upload_frame.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            file_paths, _ = QFileDialog.getOpenFileNames(self, "Select Files")
            self.add_files(file_paths)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        self.add_files(files)

    def add_files(self, files):
        for file in files:
            self.ui.label_7.setVisible(True)
            self.filename = file.split("/")[-1]
            self.ui.label_7.setText(f"Dataset Load with file name : {self.filename}")
            # file read
            self.df = pd.read_csv(f"{file}")
            # problem statement analysis
            self.ui.load_data.clicked.connect(self.load_data_in_pipeline)
            self.ui.label_8.setVisible(True)
            self.ui.label_8.setText("Analysing Problem Statement...")
   
    def load_data_in_pipeline(self):
        self.ui.listWidget.clear()
        self.ui.listWidget_2.clear()
        self.ui.listWidget_3.clear()
        self.ui.listWidget_5.clear()
        self.ui.comboBox.clear()
        self.promt = self.ui.promt_input.text()
        self.problem_type = self.pipeliner.analyze_problem_statement(self.promt)
        self.ui.label_8.setText(f"Problem Statement Type is {self.problem_type}")
        self.ui.label_9.setVisible(True)
        self.target_col, self.feature_cols = self.pipeliner.identify_features(self.df, self.promt)
        self.ui.label_9.setText(f"Identified Fearures: {self.target_col} is target column")
        self.ui.label_10.setVisible(True)
        self.df_processed = self.pipeliner.preprocess_data(self.df)
        self.ui.goto_dashboard.setVisible(True)

        # Start thread
        self.worker = Worker(self.df_processed, self.feature_cols, self.target_col, self.problem_type, self.pipeliner)
        self.worker.finished.connect(self.handle_training_results)
        self.worker.error.connect(self.handle_thread_error)
        # self.worker.output.connect(self.train_test_param)

        thread = threading.Thread(target=self.worker.run)
        thread.start()

    # @Slot(dict)
    # def train_test_param(self,X_train, X_test, y_train, y_test):
    #     self.X_train = X_train
    #     self.X_test = X_test
    #     self.y_train = y_train
    #     self.y_test = y_test

    @Slot(dict)
    def handle_training_results(self, trained_models, results):
        self.trained_models = trained_models

        self.training_results = results
        print(self.training_results)

    @Slot(str)
    def handle_thread_error(self, error_msg):
        QMessageBox.critical(self, "Training Error", error_msg)
    
    ##### Upload Data end with Pipeline ###

    #### data info tab start ###
    def data_info(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.data_info)
        self.ui.data_info_button_2.clicked.connect(self.dataset_info_tab)
        self.ui.feature_info_button.clicked.connect(self.feature_info_tab)
        self.ui.data_info_button_2.setChecked(True)
        self.dataset_info_tab()
    
    def dataset_info_tab(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.dataset_information_page)
        summary = []

        for col in self.df.columns:
            data = self.df[col]
            summary.append({
                'Feature': col,
                'Type': data.dtype,
                'Nulls': data.isnull().sum(),
                'Unique': data.nunique(),
                'Min': data.min() if pd.api.types.is_numeric_dtype(data) else None,
                'Max': data.max() if pd.api.types.is_numeric_dtype(data) else None,
                'Mean': data.mean() if pd.api.types.is_numeric_dtype(data) else None,
                'Mode': data.mode().iloc[0] if not data.mode().empty else None
            })
            
        summary_df = pd.DataFrame(summary)
        self.populate_summary_table(summary_df,self.ui.tableWidget)

    def feature_info_tab(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.custom_information)
        self.ui.listWidget.addItems(self.df.columns)
        self.ui.listWidget.itemClicked.connect(self.display_feature_info)

    def populate_summary_table(self,summary_df, table_widget: QTableWidget):
        table_widget.setRowCount(len(summary_df))
        table_widget.setColumnCount(len(summary_df.columns))
        table_widget.setHorizontalHeaderLabels(summary_df.columns)

        for row in range(len(summary_df)):
            for col in range(len(summary_df.columns)):
                value = summary_df.iloc[row, col]
                # Convert dicts (like Top 5 Values) to string
                if isinstance(value, dict):
                    value = ', '.join(f"{k}: {v}" for k, v in value.items())
                item = QTableWidgetItem(str(value))
                table_widget.setItem(row, col, item)
    
    def display_feature_info(self, item):
        import pandas as pd

        col = item.text()
        data = self.df[col]

        percent_missing = data.isnull().sum() / len(data) * 100
        cardinality = data.nunique()
        high_card = "🔺 High Cardinality" if cardinality > len(data) * 0.5 else ""

        iqr_info = ""
        if pd.api.types.is_numeric_dtype(data):
            q1 = data.quantile(0.25)
            q3 = data.quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            outliers = ((data < lower_bound) | (data > upper_bound)).sum()
            iqr_info = f"<b>Outliers:</b> {outliers} (IQR method)<br>"

        # Mode
        mode_val = data.mode()
        mode_info = f"<b>Mode:</b> {mode_val[0]}<br>" if not mode_val.empty else ""

        # Top 5 Values
        top_values = data.value_counts().head(5).to_dict()
        top_vals_html = "<b>Top 5 Values:</b><br>" + "<br>".join(f"{val}: {count}" for val, count in top_values.items())

        # Extra info panel (right)
        extra_info = f"""
        {top_vals_html}<br><br>
        <b>% Missing:</b> {percent_missing:.2f}%<br>
        <b>{high_card}</b><br>
        {iqr_info}
        """

        # Main HTML with side-by-side layout using flexbox
        info = f"""
        <div style='display:flex; justify-content:space-between; gap:40px;'>
            <div style='flex:2;'>
                <h3 style='color:#0078d7;'>{col}</h3>
                <b>Type:</b> {data.dtype}<br>
                <b>Missing:</b> {data.isnull().sum()}<br>
                <b>Unique:</b> {data.nunique()}<br>
                {f'<b>Min:</b> {data.min()}<br>' if pd.api.types.is_numeric_dtype(data) else ''}
                {f'<b>Max:</b> {data.max()}<br>' if pd.api.types.is_numeric_dtype(data) else ''}
                {f'<b>Mean:</b> {data.mean():.2f}<br>' if pd.api.types.is_numeric_dtype(data) else ''}
                {f'<b>Std Dev:</b> {data.std():.2f}<br>' if pd.api.types.is_numeric_dtype(data) else ''}
                {f'<b>Median:</b> {data.median()}<br>' if pd.api.types.is_numeric_dtype(data) else ''}
                {mode_info}
            </div>
            <div style='flex:1; background:#f9f9f9; padding:10px; border-left:2px solid #ddd;'>
                {extra_info}
            </div>
        </div>
        """

        self.ui.textEdit.setHtml(info)
    ##### data info tab end ###

    ##### visualisation tab start ####
    def visualisation_page(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.visualisation)
        self.ui.preset_button.clicked.connect(self.preset_chart_tab)
        self.ui.custom_dashboard_button.clicked.connect(self.custom_dashboard_tab)
        self.ui.preset_button.setChecked(True)
        self.preset_chart_tab()
    
    def preset_chart_tab(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.preset_chart_page)
        self.ui.listWidget_3.clear()
        self.ui.listWidget_3.addItems(self.df.columns)
        self.ui.listWidget_3.itemClicked.connect(self.display_feature_info_vis)
    
    def custom_dashboard_tab(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.custom_chart_page)
        self.ui.listWidget_2.addItems(self.df.columns)
        self.ui.listWidget_2.setSelectionMode(QListWidget.MultiSelection)
        self.ui.comboBox.addItems([
            "Histogram", "Boxplot", "Scatter Plot", "Violin Plot", "Count Plot"
        ])
        self.ui.generate_button.clicked.connect(self.generate_chart)

    def display_feature_info_vis(self, item):
        col = item.text()
        if self.df is not None:
            self.visualize_feature(self.df, col)

    def visualize_feature(self, df: pd.DataFrame, column: str):
        plt.clf()
        plt.figure(figsize=(6, 4))
        sns.set_theme(style="whitegrid")

        dtype = df[column].dtype
        unique_count = df[column].nunique()

        try:
            if pd.api.types.is_numeric_dtype(dtype):
                if unique_count < 10:
                    sns.countplot(x=column, data=df)
                    plt.title(f"Count Plot: {column}")
                else:
                    sns.histplot(df[column].dropna(), kde=True, bins=30, color="skyblue")
                    plt.title(f"Histogram: {column}")
            elif pd.api.types.is_categorical_dtype(dtype) or dtype == object:
                if unique_count <= 10:
                    df[column].value_counts().plot.pie(autopct='%1.1f%%', figsize=(5, 5))
                    plt.ylabel('')
                    plt.title(f"Pie Chart: {column}")
                else:
                    sns.countplot(y=column, data=df, order=df[column].value_counts().index[:10])
                    plt.title(f"Top 10 Categories: {column}")
            elif pd.api.types.is_datetime64_any_dtype(dtype):
                df[column].value_counts().sort_index().plot()
                plt.title(f"Time Series: {column}")
                plt.xlabel("Date")
                plt.ylabel("Count")
            else:
                self.ui.label_17.setText("❌ Unsupported data type for visualization.")
                return

            img_path = "feature_plot.png"
            plt.tight_layout()
            plt.savefig(img_path)
            self.ui.label_17.setPixmap(QPixmap(img_path))
        except Exception as e:
            self.ui.label_17.setText(f"⚠️ Error generating plot: {e}")

    def generate_chart(self):
        if self.df is None:
            QMessageBox.warning(self, "No Data", "Please load a dataset first.")
            return

        selected_items = self.ui.listWidget_2.selectedItems()
        selected_columns = [item.text() for item in selected_items]

        if not selected_columns:
            QMessageBox.warning(self, "No Feature", "Select at least one feature.")
            return

        chart = self.ui.comboBox.currentText()

        plt.clf()
        plt.figure(figsize=(6, 4))
        sns.set_theme(style="whitegrid")

        try:
            if chart == "Histogram":
                for col in selected_columns:
                    if pd.api.types.is_numeric_dtype(self.df[col]):
                        sns.histplot(self.df[col], kde=True, label=col)
                plt.legend()
                plt.title("Histogram")

            elif chart == "Boxplot":
                if len(selected_columns) == 1:
                    sns.boxplot(y=self.df[selected_columns[0]])
                else:
                    sns.boxplot(data=self.df[selected_columns])
                plt.title("Boxplot")

            elif chart == "Violin Plot":
                if len(selected_columns) == 1:
                    sns.violinplot(y=self.df[selected_columns[0]])
                elif len(selected_columns) == 2:
                    sns.violinplot(x=self.df[selected_columns[0]], y=self.df[selected_columns[1]])
                else:
                    raise Exception("Violin Plot supports only 1 or 2 features.")

            elif chart == "Scatter Plot":
                if len(selected_columns) != 2:
                    raise Exception("Scatter Plot requires exactly 2 features.")
                sns.scatterplot(
                    x=self.df[selected_columns[0]], y=self.df[selected_columns[1]]
                )
                plt.title("Scatter Plot")

            elif chart == "Count Plot":
                if len(selected_columns) != 1:
                    raise Exception("Count Plot supports only 1 categorical feature.")
                sns.countplot(x=self.df[selected_columns[0]])
                plt.title("Count Plot")

            else:
                raise Exception("Unsupported chart type.")

            plt.tight_layout()
            plot_path = "custom_plot.png"
            plt.savefig(plot_path)
            self.ui.label_22.setPixmap(QPixmap(plot_path))

        except Exception as e:
            QMessageBox.critical(self, "Plot Error", str(e))

    ##### visualisation tab end ####

    def model_training_page(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page)
        # self.ui.preset_button_2.clicked.connect(self.pretrained_tab)
        # self.ui.custom_dashboard_button_2.clicked.connect(self.custom_training_tab)
        # self.ui.preset_button_2.setChecked(True)
        # self.pretrained_tab()
        if not self.training_results:
            self.ui.generate_button_4.setVisible(False)
            self.ui.label_33.setText("Training is happening in the background")
        else:
            self.ui.generate_button_4.setVisible(True)
            # self.ui.label_33.setText(f"{self.training_results}")
            self.ui.listWidget_5.addItems(self.training_results.keys())
            self.ui.listWidget_5.itemClicked.connect(self.display_model_information)


    def pretrained_tab(self):
        self.ui.stackedWidget_5.setCurrentWidget(self.ui.preset_chart_page_2)
        self.ui.generate_button_3.clicked.connect(self.save_model)
    
    def custom_training_tab(self):
        self.ui.stackedWidget_5.setCurrentWidget(self.ui.custom_chart_page_2)
        self.ui.comboBox_3.clear()
        self.ui.comboBox_3.addItems(MODEL_PARAMS.keys())
        self.ui.comboBox_3.currentTextChanged.connect(self.update_model_options)
        self.update_model_options(self.ui.comboBox_3.currentText())
        # self.ui.comboBox_2.currentTextChanged.connect(self.on_model_selected)
        # self.on_model_selected(self.ui.comboBox_2.currentText())
    def update_model_options(self,problem_type):
        # problem_type = self.ui.comboBox_3.currentText()
        self.ui.comboBox_2.clear()
        self.ui.comboBox_2.addItems(MODEL_PARAMS[problem_type].keys())
        self.ui.comboBox_2.currentTextChanged.connect(self.on_model_selected)
        self.on_model_selected(self.ui.comboBox_2.currentText())

    def on_model_selected(self, model_name):
        params_list = []
        problem_type = self.ui.comboBox_3.currentText()
        # model = self.ui.comboBox_2.currentText()
        print(problem_type,model_name)
        print("breakkkkk")
        params = MODEL_PARAMS[problem_type].get(model_name, {})
        for param_name, param_type in params.items():
            # print(param_name,param_type)
            params_list.append(param_name)
        print("param listt",params_list)
        self.ui.label_11.setText(params_list[0])
        self.ui.label_27.setText(params_list[1])
        self.ui.generate_button_2.clicked.connect(self.custom_model_training)

    def custom_model_training(self):
        problem_type = self.ui.comboBox_3.currentText()
        model_name = self.ui.comboBox_2.currentText()
        input_1 = self.ui.lineEdit.text()
        input_2 = self.ui.lineEdit_2.text()
        trainable_params = {}
        param_keys = []
        params = MODEL_PARAMS[problem_type].get(model_name, {})
        for param,value in params.items():
            param_keys.append(param)
        trainable_params[param_keys[0]]  = input_1
        trainable_params[param_keys[1]]  = input_2
        print(params,type(params))
        score = train_custom_model(problem_type, model_name, trainable_params, self.X_train, self.X_test, self.y_train, self.y_test)
        print(score)
        print(problem_type,model_name,input_1,input_2)
    
    def save_model(self):
        self.pipeliner.save_models(self.trained_models)
        
    def display_model_information(self, item):
        model_name = item.text()
        error = self.training_results.get(model_name, "N/A")
        accuracy = 100.0 - float(error) if isinstance(error, (int, float, str)) and str(error).replace('.', '', 1).isdigit() else "N/A"
        
        # Match model name key
        name_key = model_name.lower().replace(" ", "_")
        if "random_forest" in name_key:
            if "classifier" in name_key:
                name_key = "random_forest_classifier"
            else:
                name_key = "random_forest_regressor"

        defaults = DEFAULT_MODEL_PARAMS.get(name_key, {})
        param_text = "\n".join([f"{k}: {v}" for k, v in defaults.items()]) or "No parameters available"

        display_text = f"Model: {model_name}\n\nError: {error}\nAccuracy: {accuracy}\n\nDefault Parameters:\n{param_text}"
        self.ui.label_33.setText(display_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application
    window = MainWindow()         # Create the main window
    window.show()                 # Show the main window
    sys.exit(app.exec())  