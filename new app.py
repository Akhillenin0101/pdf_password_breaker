import sys
import itertools
import PyPDF2
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog
)


class PDFBruteForceApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("PDF Password Brute Force")
        self.setGeometry(100, 100, 400, 200)

        # Layout
        self.layout = QVBoxLayout()

        # File selection button
        self.file_button = QPushButton("Select PDF File")
        self.file_button.clicked.connect(self.browse_file)
        self.layout.addWidget(self.file_button)

        # Label to display selected file
        self.file_label = QLabel("No file selected")
        self.layout.addWidget(self.file_label)

        # Input field for base word
        self.base_word_input = QLineEdit(self)
        self.base_word_input.setPlaceholderText("Enter base word (e.g., ' my password')")
        self.layout.addWidget(self.base_word_input)

        # Start button to brute force
        self.start_button = QPushButton("Start Brute Force")
        self.start_button.clicked.connect(self.start_brute_force)
        self.layout.addWidget(self.start_button)

        # Label to display results
        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        # Set layout
        self.setLayout(self.layout)

        # Variable to store selected file path
        self.pdf_file = None

    def browse_file(self):
        # Open file dialog to select a PDF file
        file_name, _ = QFileDialog.getOpenFileName(self, "Select PDF File", "", "PDF Files (*.pdf)")
        if file_name:
            self.pdf_file = file_name
            self.file_label.setText(f"Selected File: {file_name}")
        else:
            self.file_label.setText("No file selected")

    def start_brute_force(self):
        if not self.pdf_file:
            self.result_label.setText("Please select a PDF file first.")
            return

        base_word = self.base_word_input.text().strip()
        if not base_word:
            self.result_label.setText("Please enter a base word.")
            return

        # Run the brute force function
        self.result_label.setText("Brute force started...")
        QApplication.processEvents()

        password = brute_force_pdf_password(self.pdf_file, base_word)
        if password:
            self.result_label.setText(f"Password found: {password}")
        else:
            self.result_label.setText("Password not found.")

# Brute force function
def brute_force_pdf_password(pdf_file, base_word="akhil", max_number_length=9):
    # Try appending numbers to the base word
    with open(pdf_file, 'rb') as pdf:
        pdf_reader = PyPDF2.PdfReader(pdf)
        
        if not pdf_reader.is_encrypted:
            return "The file is not encrypted."
        
        # Generate password guesses by appending numbers to the base word
        for length in range(1, max_number_length + 1):
            for guess in itertools.product('0123456789', repeat=length):
                number_suffix = ''.join(guess)
                guess_password = base_word + number_suffix
                
                try:
                    if pdf_reader.decrypt(guess_password):  # Decrypt returns 1 on success
                        # If decryption is successful
                        return guess_password
                except:
                    continue
    
    return None


# Main application loop
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFBruteForceApp()
    window.show()
    sys.exit(app.exec_())
