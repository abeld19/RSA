import math
import time
import sys

class Charlie:
    def __init__(self):
        pass

    def intercept_message(self, ciphertext, alice_e, alice_n, bob_e, bob_n):
        """
        Simulate intercepting the message, Alice's public key, and Bob's public key.
        """
        print("Charlie intercepts the following:")
        print("Ciphertext:", ciphertext)
        print("Alice's Public Key (e, n):", (alice_e, alice_n))
        print("Bob's Public Key (e, n):", (bob_e, bob_n))

    def brute_force_decrypt(self, ciphertext, public_key_e, public_key_n, timeout=30):
        """
        Attempt to decrypt the message by factoring n to find the private key.
        Includes a loading bar and timeout mechanism.
        """
        print("\nCharlie attempts to brute-force decrypt the message...")
        start_time = time.time()
        max_factor = int(math.sqrt(public_key_n)) + 1
        progress_bar_length = 30

        for i in range(2, max_factor):
            # Simulate loading bar progress
            progress = (i / max_factor) * 100
            bar = "=" * int(progress / (100 / progress_bar_length))
            sys.stdout.write(f"\r[{bar:<{progress_bar_length}}] {progress:.2f}%")
            sys.stdout.flush()

            # Check for timeout
            if time.time() - start_time > timeout:
                print("\n\nCharlie took too much time. He gives up.")
                return

            if public_key_n % i == 0:
                # Factor found
                p = i
                q = public_key_n // i
                phi = (p - 1) * (q - 1)
                d = pow(public_key_e, -1, phi)
                decrypted_message = ''.join(chr(pow(c, d, public_key_n)) for c in ciphertext)
                print(f"\n\nCharlie successfully decrypted the message: {decrypted_message}")
                return

        print("\n\nCharlie failed to decrypt the message.")
