import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox
from googletrans import Translator, LANGUAGES

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Text Translator')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.input_label = QLabel('Enter text to translate:')
        self.input_text = QLineEdit()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)

        # Add dropdown list with destination languages
        self.dest_label = QLabel('Select destination language:')
        self.dest_combobox = QComboBox()
        for lang_code, lang_name in LANGUAGES.items():
            self.dest_combobox.addItem(lang_name, lang_code)
        layout.addWidget(self.dest_label)
        layout.addWidget(self.dest_combobox)

        self.translate_button = QPushButton('Translate')
        self.translate_button.clicked.connect(self.translate_text)
        layout.addWidget(self.translate_button)

        self.output_label = QLabel('Translated text:')
        self.output_text = QLabel('')
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_text)



        self.setLayout(layout)

    def translate_text(self):
        text_to_translate = self.input_text.text().strip()
        if text_to_translate:
            translator = Translator()
            dest_language_code = self.dest_combobox.currentData()
            translated_text = translator.translate(text_to_translate, dest=dest_language_code)
            self.output_text.setText(translated_text.text)
        else:
            QMessageBox.warning(self, 'Warning', 'Please enter text to translate.')

def main():
    app = QApplication(sys.argv)
    translator_app = TranslatorApp()
    translator_app.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()