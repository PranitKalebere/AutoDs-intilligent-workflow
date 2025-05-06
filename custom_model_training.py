import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QComboBox, QFormLayout, QLineEdit, QPushButton, QMessageBox
)

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


class HyperParamUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Model Hyperparameter Configuration")
        self.setMinimumWidth(400)

        self.problem_type_cb = QComboBox()
        self.problem_type_cb.addItems(MODEL_PARAMS.keys())
        self.problem_type_cb.currentTextChanged.connect(self.update_model_options)

        self.model_cb = QComboBox()
        self.model_cb.currentTextChanged.connect(self.update_param_fields)

        self.param_form = QFormLayout()
        self.param_inputs = {}

        self.submit_btn = QPushButton("Get Parameters")
        self.submit_btn.clicked.connect(self.collect_params)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Select Problem Type:"))
        layout.addWidget(self.problem_type_cb)
        layout.addWidget(QLabel("Select Model:"))
        layout.addWidget(self.model_cb)
        layout.addLayout(self.param_form)
        layout.addWidget(self.submit_btn)

        self.setLayout(layout)
        self.update_model_options()

    def update_model_options(self):
        problem_type = self.problem_type_cb.currentText()
        self.model_cb.clear()
        self.model_cb.addItems(MODEL_PARAMS[problem_type].keys())
        self.update_param_fields()

    def update_param_fields(self):
        # Clear old fields
        for i in reversed(range(self.param_form.count())):
            self.param_form.itemAt(i).widget().deleteLater()
        self.param_inputs.clear()

        problem_type = self.problem_type_cb.currentText()
        model = self.model_cb.currentText()
        params = MODEL_PARAMS[problem_type].get(model, {})

        for param_name, param_type in params.items():
            field = QLineEdit()
            field.setPlaceholderText(f"{param_type.__name__}")
            self.param_form.addRow(QLabel(param_name), field)
            self.param_inputs[param_name] = (field, param_type)

    def collect_params(self):
        params = {}
        try:
            for key, (line_edit, typ) in self.param_inputs.items():
                val_str = line_edit.text()
                if val_str == "":
                    raise ValueError(f"{key} is required.")
                params[key] = typ(val_str)
            QMessageBox.information(self, "Collected Parameters", str(params))
        except ValueError as e:
            QMessageBox.critical(self, "Input Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HyperParamUI()
    window.show()
    sys.exit(app.exec())
