import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox
)

class VowelCounterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vowel Counter")
        self.setGeometry(100, 100, 300, 150)

        # Create widgets
        self.label = QLabel("Enter a word:")
        self.input_field = QLineEdit()
        self.button = QPushButton("Count Vowels")
        self.result_label = QLabel("")

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        # Connect button click to function
        self.button.clicked.connect(self.count_vowels)

    def count_vowels(self):
        text = self.input_field.text()
        vowels = "aeiouAEIOU"
        count = sum(1 for char in text if char in vowels)

        self.result_label.setText(f"Vowel count: {count}")

        # Optional: show a message box
        # QMessageBox.information(self, "Result", f"Vowel count: {count}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VowelCounterApp()
    window.show()
    sys.exit(app.exec_())
