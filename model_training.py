from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QFormLayout,
    QLabel, QLineEdit, QMessageBox
)
import sys

# Model parameter definitions
MODEL_PARAMS = {
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
}

class ModelTrainerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Model Trainer")

        self.layout = QVBoxLayout()

        # Model selection
        self.model_select = QComboBox()
        self.model_select.addItems(MODEL_PARAMS.keys())
        self.model_select.currentTextChanged.connect(self.on_model_selected)
        self.layout.addWidget(QLabel("Select Model:"))
        self.layout.addWidget(self.model_select)

        # Dynamic parameter form
        self.param_form = QFormLayout()
        self.layout.addLayout(self.param_form)

        # Train button
        self.train_button = QPushButton("Train Model")
        self.train_button.clicked.connect(self.on_train_clicked)
        self.layout.addWidget(self.train_button)

        self.setLayout(self.layout)

        # For tracking input fields
        self.param_inputs = {}

        # Initialize form
        self.on_model_selected(self.model_select.currentText())

    def clear_param_inputs(self):
        while self.param_form.rowCount():
            self.param_form.removeRow(0)
        self.param_inputs = {}

    def on_model_selected(self, model_name):
        self.clear_param_inputs()
        for param, param_type in MODEL_PARAMS[model_name].items():
            input_field = QLineEdit()
            input_field.setPlaceholderText(f"Enter {param} ({param_type.__name__})")
            self.param_form.addRow(QLabel(param), input_field)
            self.param_inputs[param] = (input_field, param_type)

    def get_custom_params(self):
        params = {}
        for param, (widget, param_type) in self.param_inputs.items():
            try:
                value = param_type(widget.text())
                params[param] = value
            except ValueError:
                QMessageBox.warning(self, "Invalid Input", f"Invalid value for {param}")
                return None
        return params

    def on_train_clicked(self):
        model_name = self.model_select.currentText()
        params = self.get_custom_params()
        if params is not None:
            QMessageBox.information(self, "Training Info", f"Model: {model_name}\nParams: {params}")
            # Here you would call your actual training function with `params`

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ModelTrainerGUI()
    window.show()
    sys.exit(app.exec())
