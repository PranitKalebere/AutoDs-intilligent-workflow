import sys
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QListWidget, QTextEdit, QLabel, QFileDialog, QPushButton
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class DatasetExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dataset Explorer")
        self.setMinimumSize(900, 600)

        self.layout = QVBoxLayout(self)

        self.load_button = QPushButton("Load CSV Dataset")
        self.load_button.clicked.connect(self.load_dataset)
        self.layout.addWidget(self.load_button)

        self.feature_list = QListWidget()
        self.feature_list.itemClicked.connect(self.display_feature_info)
        self.layout.addWidget(self.feature_list)

        self.info_box = QTextEdit()
        self.info_box.setReadOnly(True)
        self.layout.addWidget(self.info_box)

        self.plot_label = QLabel()
        self.plot_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.plot_label)

        self.df = None

    def load_dataset(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if file_path:
            self.df = pd.read_csv(file_path)
            self.feature_list.clear()
            self.feature_list.addItems(self.df.columns)

    def display_feature_info(self, item):
        col = item.text()
        if self.df is not None:
            info = self.get_feature_info(self.df, col)
            self.info_box.setPlainText(info)
            self.visualize_feature(self.df, col)

    def get_feature_info(self, df, col):
        dtype = df[col].dtype
        unique_vals = df[col].nunique()
        missing = df[col].isnull().sum()
        desc = df[col].describe(include='all')

        info = f"📊 Feature: {col}\n"
        info += f"Data Type: {dtype}\n"
        info += f"Unique Values: {unique_vals}\n"
        info += f"Missing Values: {missing}\n\n"
        info += f"{desc.to_string()}\n"
        return info

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
                self.plot_label.setText("❌ Unsupported data type for visualization.")
                return

            img_path = "feature_plot.png"
            plt.tight_layout()
            plt.savefig(img_path)
            self.plot_label.setPixmap(QPixmap(img_path))
        except Exception as e:
            self.plot_label.setText(f"⚠️ Error generating plot: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = DatasetExplorer()
    viewer.show()
    sys.exit(app.exec())
