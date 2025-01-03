import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
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

    def log_to_charlie(self, message):
        """Log a message to the Charlie output box."""
        self.charlie_output.append(message)

    def initUI(self):
        main_layout = QHBoxLayout()

        # Alice Section (Sender)
        alice_layout = QVBoxLayout()
        alice_layout.addWidget(QLabel("Alice (Sender)"))

        self.alice_output = QTextEdit()
        self.alice_output.setReadOnly(True)
        alice_layout.addWidget(self.alice_output)

        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Enter a message to encrypt")
        alice_layout.addWidget(self.message_input)

        self.encrypt_button = QPushButton("Send/Encrypt")
        self.encrypt_button.clicked.connect(self.encrypt_message)
        alice_layout.addWidget(self.encrypt_button)

        # Bob Section (Receiver)
        bob_layout = QVBoxLayout()
        bob_layout.addWidget(QLabel("Bob (Receiver)"))

        self.bob_output = QTextEdit()
        self.bob_output.setReadOnly(True)
        bob_layout.addWidget(self.bob_output)

        self.decrypt_button = QPushButton("Decrypt")
        self.decrypt_button.clicked.connect(self.decrypt_message)
        bob_layout.addWidget(self.decrypt_button)

        # Charlie Section (Intercept)
        charlie_layout = QVBoxLayout()
        charlie_layout.addWidget(QLabel("Charlie (Intercept)"))

        self.charlie_output = QTextEdit()
        self.charlie_output.setReadOnly(True)
        charlie_layout.addWidget(self.charlie_output)

        self.charlie_button = QPushButton("Simulate Charlie")
        self.charlie_button.clicked.connect(self.simulate_charlie)
        charlie_layout.addWidget(self.charlie_button)

        # Add sections to the main layout
        main_layout.addLayout(alice_layout, stretch=1)
        main_layout.addLayout(bob_layout, stretch=1)
        main_layout.addLayout(charlie_layout, stretch=1)

        # Set central widget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def encrypt_message(self):
        message = self.message_input.text()
        if not message:
            self.alice_output.append("Please enter a message to encrypt.\n")
            return

        # Encrypt the message
        self.ciphertext = self.alice.encrypt(message, self.bob.e, self.bob.n)
        self.alice_output.append(f"Encrypted Message: {self.ciphertext}\n")

    def decrypt_message(self):
        if not self.ciphertext:
            self.bob_output.append("No message to decrypt.\n")
            return

        # Decrypt the message
        decrypted_message = self.bob.decrypt(self.ciphertext)
        self.bob_output.append(f"Decrypted Message: {decrypted_message}\n")

    def simulate_charlie(self):
        if not self.ciphertext:
            self.charlie_output.append("No message for Charlie to intercept.\n")
            return

        # Simulate Charlie's interception
        self.charlie.intercept_message(
            self.ciphertext, self.alice.e, self.alice.n, self.bob.e, self.bob.n
        )
        self.charlie.brute_force_decrypt(self.ciphertext, self.bob.e, self.bob.n)

        # Convert list to a single string
        self.charlie_output.append("\n" + "\n".join(self.charlie.get_logged_messages()) + "\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RSAApp()
    window.show()
    sys.exit(app.exec())
