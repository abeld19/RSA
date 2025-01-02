import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from Alice import Alice
from Bob import Bob
from Charlie import Charlie


class RSAApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RSA Encryption/Decryption GUI")

        # Instances of Alice, Bob, and Charlie
        self.alice = Alice()
        self.bob = Bob()
        self.charlie = Charlie()
        self.ciphertext = None

        # Initialize UI
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Message input
        self.message_label = QLabel("Enter a message to encrypt:")
        layout.addWidget(self.message_label)

        self.message_input = QLineEdit()
        layout.addWidget(self.message_input)

        # Encrypt button
        self.encrypt_button = QPushButton("Encrypt")
        self.encrypt_button.clicked.connect(self.encrypt_message)
        layout.addWidget(self.encrypt_button)

        # Decrypt button
        self.decrypt_button = QPushButton("Decrypt")
        self.decrypt_button.clicked.connect(self.decrypt_message)
        layout.addWidget(self.decrypt_button)

        # Simulate Charlie
        self.charlie_button = QPushButton("Simulate Charlie")
        self.charlie_button.clicked.connect(self.simulate_charlie)
        layout.addWidget(self.charlie_button)

        # Output display
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        # Set central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def encrypt_message(self):
        message = self.message_input.text()
        if not message:
            self.output_text.append("Please enter a message to encrypt.\n")
            return

        # Encrypt the message
        self.ciphertext = self.alice.encrypt(message, self.bob.e, self.bob.n)
        self.output_text.append(f"Encrypted Message: {self.ciphertext}\n")

    def decrypt_message(self):
        if not self.ciphertext:
            self.output_text.append("No message to decrypt.\n")
            return

        # Decrypt the message
        decrypted_message = self.bob.decrypt(self.ciphertext)
        self.output_text.append(f"Decrypted Message: {decrypted_message}\n")

    def simulate_charlie(self):
        if not self.ciphertext:
            self.output_text.append("No message for Charlie to intercept.\n")
            return

        # Simulate Charlie's interception
        self.charlie.intercept_message(
            self.ciphertext, self.alice.e, self.alice.n, self.bob.e, self.bob.n
        )
        self.charlie.brute_force_decrypt(self.ciphertext, self.bob.e, self.bob.n)
        self.output_text.append("Charlie attempted to decrypt the message.\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RSAApp()
    window.show()
    sys.exit(app.exec())
