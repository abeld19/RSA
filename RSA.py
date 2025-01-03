from Alice import Alice;
from Bob import Bob
from Charlie import Charlie

class menu:

    TITLE = (
        "\n2910326 Computer Security coursework\n"
        + " by Ahmet Toplu and Abel Daniel\n\n"
        + "\t********************\n"
        + "\t1. Question 1 \n"
        + "\t2. Question 2 \n"
        + "\t3. Question 3 \n"
        + "\t4. no attempt \n"
        + "\t0. Exit \n"
        + "\t********************\n"
        + "Please input a single digit (0-4):\n"
    )

    def __init__(self):
        selected = -1
        while selected != 0:
            print(self.TITLE)
          
            try:
                selected = int(input())
               
                if selected == 1:
                    self.q1()
                elif selected == 2:
                    self.q2()
                elif selected == 3:
                    self.q3()
                elif selected == 4:
                    self.q4()
               
            except Exception as ex:
          
                pass

    def q1(self):
        print("in q1")

        # Alice, Bob, and Charlie are the three parties involved in the RSA encryption scheme.
        alice = Alice()
        bob = Bob()
        charlie = Charlie()

        # Alice and Bob generate their RSA key pairs
        print("Alice's Public Key (e, n):", (alice.e, alice.n))
        print("Bob's Public Key (e, n):", (bob.e, bob.n))
        
        # Alice encrypts a message to send to Bob
        message = input("Enter a message to encrypt: ")
        ciphertext = alice.encrypt(message, bob.e, bob.n)
        print("Encrypted message (ciphertext):", ciphertext)

        # Charlie intercepts the communication
        charlie.intercept_message(ciphertext, alice.e, alice.n, bob.e, bob.n)
        
        # Charlie attempts to brute-force decrypt the message
        charlie.brute_force_decrypt(ciphertext, bob.e, bob.n)
        
        # Bob decrypts the message
        decrypted_message = bob.decrypt(ciphertext)
        print("Bob decrypted the message:", decrypted_message)

    def q2(self):
        print("in q2")

    def q3(self):
        print("in q3")
        return 1

    def q4(self):
        print("in q4")
        return True

if __name__ == "__main__":
    menu()
