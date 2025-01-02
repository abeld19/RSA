import math

class Bob:
    def __init__(self):
        pass

    def generate_private_key(self, e, r):
        """Generate the private key (d) using the modular inverse of e mod r."""
        def gcd_extended(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = gcd_extended(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y

        gcd, x, _ = gcd_extended(e, r)
        if gcd != 1:
            raise ValueError("e and r are not coprime")
        return x % r

    def encrypt(self, plaintext, e, n):
        """Encrypt the plaintext using the public key (e, n)."""
        return [pow(ord(char), e, n) for char in plaintext]

    def decrypt(self, ciphertext, d, n):
        """Decrypt the ciphertext using the private key d and modulus n."""
        return ''.join(chr(pow(c, d, n)) for c in ciphertext)

    def run(self, p, q, e, plaintext):
        """Run the RSA encryption and decryption process."""
        # Compute n and r
        n = p * q
        r = (p - 1) * (q - 1)

        # Generate private key
        d = self.generate_private_key(e, r)

        # Display keys
        print("Public Key (e, n):", (e, n))
        print("Private Key (d, n):", (d, n))

        # Encrypt the plaintext
        ciphertext = self.encrypt(plaintext, e, n)
        print("Ciphertext (ASCII values):", ciphertext)

        # Decrypt the ciphertext
        decrypted_message = self.decrypt(ciphertext, d, n)
        print("Decrypted message:", decrypted_message)