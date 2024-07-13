import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class BMICalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create layout
        layout = QVBoxLayout()

        # Add widgets to layout
        self.weight_input = QLineEdit()
        self.height_input = QLineEdit()
        self.calculate_button = QPushButton('Calculate BMI')
        self.result_label = QLabel('')

        layout.addWidget(QLabel('Weight (kg):'))
        layout.addWidget(self.weight_input)
        layout.addWidget(QLabel('Height (cm):'))
        layout.addWidget(self.height_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        # Set the layout on the application's window
        self.setLayout(layout)

        # Connect the button's click signal to the calculate_bmi method
        self.calculate_button.clicked.connect(self.calculate_bmi)

        # Set the window title and show the window
        self.setWindowTitle('BMI Calculator')
        self.show()

    def calculate_bmi(self):
        # Get the user input
        weight = float(self.weight_input.text())
        height = float(self.height_input.text()) / 100  # convert cm to meters

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Display the result
        self.result_label.setText(f'Your BMI: {bmi:.2f}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BMICalculatorApp()
    sys.exit(app.exec())