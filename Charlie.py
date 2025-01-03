import math
import time

class Charlie:
    def __init__(self, log_callback=None):
        self.log_callback = log_callback or self.default_log
        self.logged_messages = []

    def default_log(self, message):
        """Default log function that appends to logged messages."""
        self.logged_messages.append(message)

    def log(self, message):
        """Log a message using the callback."""
        self.log_callback(message)

    def intercept_message(self, ciphertext, alice_e, alice_n, bob_e, bob_n):
        """
        Simulate intercepting the message, Alice's public key, and Bob's public key.
        """
        self.log("Charlie intercepts the following:")
        self.log(f"Ciphertext: {ciphertext}")
        self.log(f"Alice's Public Key (e, n): ({alice_e}, {alice_n})")
        self.log(f"Bob's Public Key (e, n): ({bob_e}, {bob_n})")

    def brute_force_decrypt(self, ciphertext, public_key_e, public_key_n, timeout=10):
        """
        Attempt to decrypt the message by factoring n to find the private key.
        Includes a loading bar and timeout mechanism.
        """
        self.log("\nCharlie attempts to brute-force decrypt the message...")
        start_time = time.time()
        max_factor = int(math.sqrt(public_key_n)) + 1

        for i in range(2, max_factor):
            # Check for timeout
            if time.time() - start_time > timeout:
                self.log("\n\nCharlie took too much time. He gives up.")
                return

            if public_key_n % i == 0:
                # Factor found
                p = i
                q = public_key_n // i
                phi = (p - 1) * (q - 1)
                d = pow(public_key_e, -1, phi)
                decrypted_message = ''.join(chr(pow(c, d, public_key_n)) for c in ciphertext)
                self.log(f"\n\nCharlie successfully decrypted the message: {decrypted_message}")
                return

        self.log("\n\nCharlie failed to decrypt the message.")

    def get_logged_messages(self):
        """Return all logged messages."""
        return self.logged_messages
