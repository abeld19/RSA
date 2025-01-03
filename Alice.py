import math
import random
from sympy import randprime

class Alice:
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
      
        # 1. Generate two large primes p and q
        self.p = randprime(2**(self.bit_length - 1), 2**self.bit_length)
        self.q = randprime(2**(self.bit_length - 1), 2**self.bit_length)

        # 2. Compute n = p * q
        self.n = self.p * self.q

        # 3. Compute phi = (p - 1) * (q - 1)
        self.phi = (self.p - 1) * (self.q - 1)

        # 4. Choose e such that gcd(e, phi) = 1
        while True:
            e_candidate = random.randrange(2, self.phi)
            if math.gcd(e_candidate, self.phi) == 1:
                self.e = e_candidate
                break

        # 5. Compute d, the modular inverse of e mod phi
        self.d = pow(self.e, -1, self.phi)
        

    def encrypt(self, message, reciever_e, reciever_n):
        return [pow(ord(char), reciever_e, reciever_n) for char in message]

def main():
    # Instantiate Alice
    alice = Alice(bit_length=512)

    # Print out the public key (e, n) for demonstration
    print("=== Alice's RSA Public Key ===")
    print(f"p:     {alice.p}")
    print(f"q:     {alice.q}")
    print(f"n:     {alice.n}")
    print(f"phi:   {alice.phi}")
    print(f"e (public): {alice.e}")
    print(f"d (private): {alice.d}")  

    # Prompt the user for a message to encrypt
    msg_str = input("\nEnter a numeric message to encrypt: ")
    message = int(msg_str)

    # Encrypt
    ciphertext = alice.encrypt(message)
    print(f"\nEncrypted ciphertext: {ciphertext}")

if __name__ == "__main__":
    main()
