from PySide6.QtWidgets import (
    QApplication, QFrame, QFileDialog, QVBoxLayout, QLabel, QListWidget
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QDragEnterEvent, QDropEvent


class FileDropFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setCursor(Qt.PointingHandCursor)

        self.setStyleSheet("""
            QFrame {
                border: 2px dashed #aaa;
                border-radius: 10px;
                background-color: #f9f9f9;
            }
            QFrame:hover {
                background-color: #f0f0f0;
                border-color: #0078d7;
            }
        """)

        layout = QVBoxLayout(self)
        self.label = QLabel("Drag & drop files here\nor click to choose", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: #666; font: 14px 'Segoe UI'")
        self.list_widget = QListWidget(self)

        layout.addWidget(self.label)
        layout.addWidget(self.list_widget)

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
            self.list_widget.addItem(file)


if __name__ == "__main__":
    app = QApplication([])
    frame = FileDropFrame()
    frame.setMinimumSize(400, 300)
    frame.show()
    app.exec()
