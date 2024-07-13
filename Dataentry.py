import sys
import csv
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

class DataEntryApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Data Entry Tool')
        self.setGeometry(100, 100, 300, 100)

        # Create layout
        layout = QVBoxLayout()

        # Create input field
        self.inputField = QLineEdit(self)
        self.inputField.setPlaceholderText('Enter text here...')
        layout.addWidget(self.inputField)

        # Create submit button
        submitButton = QPushButton('Submit', self)
        submitButton.clicked.connect(self.submitData)
        layout.addWidget(submitButton)

        # Set layout
        self.setLayout(layout)

        # Connect Enter key to the submitData method
        self.inputField.returnPressed.connect(self.submitData)

    def submitData(self):
        # Get text from input field
        text = self.inputField.text()

        if not text:
            QMessageBox.warning(self, 'Warning', 'Input field cannot be empty!')
            return

        # Append text to the CSV file
        csv_file = 'data.csv'
        file_exists = os.path.isfile(csv_file)

        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                # Write the header if the file does not exist
                writer.writerow(['Text'])

            # Write the text
            writer.writerow([text])

        # Clear the input field
        self.inputField.clear()

        # Show a confirmation message
        QMessageBox.information(self, 'Success', 'Data has been added to the CSV file!')

def main():
    app = QApplication(sys.argv)
    ex = DataEntryApp()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()