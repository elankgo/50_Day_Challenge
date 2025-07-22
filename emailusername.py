import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout
)

class EmailExtractor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Email Username Extractor")
        self.setGeometry(100, 100, 400, 200)

        # Widgets
        self.label = QLabel("Enter email address:")
        self.input_field = QLineEdit()
        self.result_label = QLabel("")
        
        self.check_button = QPushButton("Check")
        self.clear_button = QPushButton("Clear")

        # Button actions
        self.check_button.clicked.connect(self.extract_username)
        self.clear_button.clicked.connect(self.clear_fields)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.check_button)
        button_layout.addWidget(self.clear_button)

        layout.addLayout(button_layout)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def extract_username(self):
        email = self.input_field.text().strip()
        if "@" in email:
            username = email.split("@")[0]
            self.result_label.setText(f"Username: {username}")
        else:
            self.result_label.setText("Invalid email format. Please include '@'.")

    def clear_fields(self):
        self.input_field.clear()
        self.result_label.setText("")

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmailExtractor()
    window.show()
    sys.exit(app.exec_())
