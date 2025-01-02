import math
import random
from sympy import randprime

class Bob:
    def __init__(self, bit_length=512):
        self.bit_length = bit_length
        self.p = None
        self.q = None
        self.n = None
        self.phi = None
        self.e = None
        self.d = None
        self.generate_keys()

    def generate_keys(self):
        """Generate Bob's RSA key pair."""
        # Generate two large primes p and q
        self.p = randprime(2**(self.bit_length - 1), 2**self.bit_length)
        self.q = randprime(2**(self.bit_length - 1), 2**self.bit_length)

        # Compute n = p * q
        self.n = self.p * self.q

        # Compute phi = (p - 1) * (q - 1)
        self.phi = (self.p - 1) * (self.q - 1)

        # Choose e such that gcd(e, phi) = 1
        while True:
            e_candidate = random.randrange(2, self.phi)
            if math.gcd(e_candidate, self.phi) == 1:
                self.e = e_candidate
                break

        # Compute d, the modular inverse of e mod phi
        self.d = pow(self.e, -1, self.phi)

    def decrypt(self, ciphertext):
        """Decrypt the ciphertext using the sender's public key (e, n)."""
        return ''.join(chr(pow(c, self.d, self.n)) for c in ciphertext)

    def run(self, sender_e, sender_n, ciphertext):
        """Run the RSA decryption process using the sender's public key."""
        print("Bob's Public Key (e, n):", (self.e, self.n))
        print("Bob's Private Key (d, n):", (self.d, self.n))
        print("Ciphertext received from sender:", ciphertext)

        # Decrypt the ciphertext using sender's public key
        decrypted_message = self.decrypt(ciphertext, sender_e, sender_n)
        print("Decrypted message:", decrypted_message)