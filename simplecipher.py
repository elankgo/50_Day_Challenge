import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout
)

class CipherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Cipher - Encrypt & Decrypt")
        self.setGeometry(100, 100, 450, 220)

        # Widgets
        self.label = QLabel("Enter a sentence:")
        self.input_field = QLineEdit()
        self.result_label = QLabel("")

        self.encrypt_button = QPushButton("Encrypt (+1)")
        self.decrypt_button = QPushButton("Decrypt (-1)")
        self.clear_button = QPushButton("Clear")

        # Button actions
        self.encrypt_button.clicked.connect(self.encrypt)
        self.decrypt_button.clicked.connect(self.decrypt)
        self.clear_button.clicked.connect(self.clear)

        # Layouts
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.encrypt_button)
        button_layout.addWidget(self.decrypt_button)
        button_layout.addWidget(self.clear_button)

        layout.addLayout(button_layout)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def shift_text(self, text, shift):
        shifted = ""
        for char in text:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                shifted += chr((ord(char) - offset + shift) % 26 + offset)
            else:
                shifted += char
        return shifted

    def encrypt(self):
        text = self.input_field.text()
        encrypted = self.shift_text(text, 1)
        self.result_label.setText(f"Encrypted: {encrypted}")

    def decrypt(self):
        text = self.input_field.text()
        decrypted = self.shift_text(text, -1)
        self.result_label.setText(f"Decrypted: {decrypted}")

    def clear(self):
        self.input_field.clear()
        self.result_label.setText("")

# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CipherApp()
    window.show()
    sys.exit(app.exec_())
