import sys
import pandas as pd
from PySide6.QtWidgets import (
    QApplication, QWidget, QListWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QLabel
)
from PySide6.QtCore import Qt

# Load your DataFrame
df = pd.read_csv("house_prices.csv")  # Replace with your dataset

class FeatureInspector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Feature Explorer")
        self.setMinimumSize(800, 500)

        # Widgets
        self.feature_list = QListWidget()
        self.feature_info = QTextEdit()
        self.feature_info.setReadOnly(True)

        # Populate feature list
        self.feature_list.addItems(df.columns)

        # Connect signal
        self.feature_list.itemClicked.connect(self.display_feature_info)

        # Layout
        layout = QHBoxLayout()
        layout.addWidget(self.feature_list, 2)
        layout.addWidget(self.feature_info, 5)
        self.setLayout(layout)

    def display_feature_info(self, item):
        col = item.text()
        data = df[col]

        info = f"<h3 style='color:#0078d7;'>{col}</h3>"
        info += f"<b>Type:</b> {data.dtype}<br>"
        info += f"<b>Missing:</b> {data.isnull().sum()}<br>"
        info += f"<b>Unique:</b> {data.nunique()}<br>"

        if pd.api.types.is_numeric_dtype(data):
            info += f"<b>Min:</b> {data.min()}<br>"
            info += f"<b>Max:</b> {data.max()}<br>"
            info += f"<b>Mean:</b> {data.mean():.2f}<br>"
            info += f"<b>Std Dev:</b> {data.std():.2f}<br>"
            info += f"<b>Median:</b> {data.median()}<br>"

        mode_val = data.mode()
        if not mode_val.empty:
            info += f"<b>Mode:</b> {mode_val[0]}<br>"

        top_values = data.value_counts().head(5).to_dict()
        info += "<br><b>Top 5 Values:</b><br>"
        for val, count in top_values.items():
            info += f"{val}: {count}<br>"

        self.feature_info.setHtml(info)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FeatureInspector()
    window.show()
    sys.exit(app.exec())
