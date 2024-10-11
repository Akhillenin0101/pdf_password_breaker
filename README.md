# PDF Password Brute Force Application (PyQt5 GUI)

This application is designed to assist users in attempting brute-force password recovery for encrypted PDF files. The GUI is built using **PyQt5** and leverages the **PyPDF2** library to decrypt password-protected PDFs by appending numeric sequences to a user-provided base word. The application provides a simple, intuitive interface for selecting a PDF, entering the base word, and initiating the brute force process.

## Features

### 1. File Selection
- Users can browse and select a PDF file using a file dialog.
- The selected file's path is displayed in the interface.

### 2. Base Word Input
- A text input allows users to specify the base word, which the program will use to generate password guesses by appending numbers.

### 3. Brute Force Attack
- Once the file and base word are provided, users can start the brute force process by clicking the "Start Brute Force" button.
- The application attempts various password combinations by attaching number sequences to the base word.

### 4. Real-Time Feedback
- A status label updates users about the ongoing process (whether brute force has started, the password is found, or no password was detected).
- If the password is successfully discovered, it is displayed on the screen.

### 5. User-Friendly Interface
- The interface is simple and clean, making it easy to operate, even for non-technical users.

## Use Case

This tool is useful when a user knows part of the password (such as a base word) but needs help brute-forcing through numeric combinations that may follow. For example, if the password format is suspected to be something like `akhil123`, the user can provide `akhil` as the base word, and the tool will try appending numbers like `akhil1`, `akhil12`, `akhil123`, etc.

## Technical Overview

- **PyQt5** is used to create the graphical user interface.
- **PyPDF2** handles the PDF decryption.
- **Itertools** is used to generate numeric combinations for the brute force attack.

With this tool, users can easily test combinations to find a password while receiving clear feedback on the status of the brute force process.

---

### Installation

To install the necessary libraries:

```bash
pip install PyQt5 PyPDF2
# Gallery of Images

![Image 1](./image1.png)
![Image 2](./image2.png)
![Image 3](./image3.png)
![Image 4](./image4.png)

