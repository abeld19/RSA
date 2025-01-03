# RSA Encryption/Decryption Application

## Introduction
This project is a demonstration of RSA encryption and decryption using a Python implementation. The program simulates three parties:

- **Alice**: Generates RSA keys and encrypts messages.
- **Bob**: Decrypts received messages.
- **Charlie**: Attempts to intercept and brute-force decrypt messages.

It provides both a terminal-based interface and a GUI application for interaction.

## Features
- RSA key generation for Alice and Bob.
- Message encryption by Alice.
- Message decryption by Bob.
- Interception and brute-force decryption simulation by Charlie.
- GUI interface built with PyQt6.

## Requirements
Ensure you have the required dependencies installed. Use the following command to install them:

```bash
pip install -r requirements.txt
```

### Dependencies
- `PyQt6`
- `sympy`

## How to Run

### Terminal Interface
To use the terminal interface, run the following command:

```bash
python RSA.py
```

You will be presented with a menu to select different options. Follow the prompts to encrypt, decrypt, or simulate interception.

### GUI Interface
To use the GUI interface, run the following command:

```bash
python gui.py
```

The GUI provides three sections:
1. **Alice (Sender)**: Input a message and encrypt it.
2. **Bob (Receiver)**: Decrypt received messages.
3. **Charlie (Intercept)**: Simulate interception and brute-force decryption.

## Project Structure
- **`Alice.py`**: Handles RSA key generation and message encryption.
- **`Bob.py`**: Handles decryption of received messages using Bob's private key.
- **`Charlie.py`**: Simulates message interception and brute-force decryption.
- **`RSA.py`**: Provides a terminal-based interface for interaction.
- **`gui.py`**: Provides a graphical user interface for the program.

## Notes
- The RSA implementation is for educational purposes and may not be suitable for production use.
- The brute-force decryption by Charlie is time-limited and demonstrates the importance of choosing secure key lengths.

## Authors
- [Ahmet Toplu](https://github.com/Ahmet-Toplu)
- [Abel Daniel](https://github.com/abeld19)
