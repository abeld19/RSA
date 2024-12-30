class menu:

    TITLE = (
        "\n2910326 Computer Security coursework\n"
        + " by firstname-FAMILYNAME_SRN\n\n"
        + "\t********************\n"
        + "\t1. Declaration: Sorry but part of the program was copied\n"
        + "from the Internet! \n"
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
