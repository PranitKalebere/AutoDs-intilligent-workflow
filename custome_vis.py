import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QListWidget, QLabel,
    QPushButton, QFileDialog, QComboBox, QHBoxLayout, QMessageBox
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class CustomVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Visualization")
        self.setMinimumSize(800, 600)

        self.df = None

        layout = QVBoxLayout(self)

        # Load dataset button
        self.load_btn = QPushButton("Load CSV")
        self.load_btn.clicked.connect(self.load_dataset)
        layout.addWidget(self.load_btn)

        # Feature selection
        self.feature_list = QListWidget()
        self.feature_list.setSelectionMode(QListWidget.MultiSelection)
        layout.addWidget(self.feature_list)

        # Chart type selection
        chart_layout = QHBoxLayout()
        self.chart_type = QComboBox()
        self.chart_type.addItems([
            "Histogram", "Boxplot", "Scatter Plot", "Violin Plot", "Count Plot"
        ])
        chart_layout.addWidget(QLabel("Chart Type:"))
        chart_layout.addWidget(self.chart_type)
        layout.addLayout(chart_layout)

        # Plot button
        self.plot_btn = QPushButton("Generate Chart")
        self.plot_btn.clicked.connect(self.generate_chart)
        layout.addWidget(self.plot_btn)

        # Display area
        self.plot_label = QLabel("Plot will appear here")
        self.plot_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.plot_label)

    def load_dataset(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if file_path:
            self.df = pd.read_csv(file_path)
            self.feature_list.clear()
            self.feature_list.addItems(self.df.columns)

    def generate_chart(self):
        if self.df is None:
            QMessageBox.warning(self, "No Data", "Please load a dataset first.")
            return

        selected_items = self.feature_list.selectedItems()
        selected_columns = [item.text() for item in selected_items]

        if not selected_columns:
            QMessageBox.warning(self, "No Feature", "Select at least one feature.")
            return

        chart = self.chart_type.currentText()

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
            self.plot_label.setPixmap(QPixmap(plot_path))

        except Exception as e:
            QMessageBox.critical(self, "Plot Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CustomVisualizer()
    win.show()
    sys.exit(app.exec())
