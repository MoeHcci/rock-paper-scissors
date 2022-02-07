#This is a command line project of rock paper scissors
import random
def rock_paper_scisors():
    #user = input("Please input either r for rock, p for paper, and s for scissors")
    computer= random.choice(['r','p','s'])
    while True:
        user = input("Please input either r for rock, p for paper, and s for scissors")
        if user == "r":
            break
        elif user == "p":
            break
        elif user == "s":
            break
        else:
            print('unacceptable input')
            user = input("Please input either r for rock, p for paper, and s for scissors")

    if user == computer:
        print ('It is a tie')
        print(f"The user's input is {user}")
        print(f"The computer's input is {computer}")
        return

    if user == 'r' and computer == "s":

        print('user won')
        print(f"The user's input is {user}")
        print(f"The computer's input is {computer}")
        return
    if user == 'r' and computer == "p":

        print('computer won')
        print(f"The user's input is {user}")
        print(f"The computer's input is {computer}")
        return
    if user == 'p' and computer == "r":

        print('user won')
        print(f"The user's input is {user}")
        print(f"The computer's input is {computer}")
        return
    if user == 'p' and computer == "s":

        print('computer won')
        print(f"The user's input is {user}")
        print(f"The computer's input is {computer}")
        return
    if user == 's' and computer == "r":

        print('computer won')
        print(f"The user's input is {user}")
        print(f"The computer's input is {computer}")
        return
    if user == 's' and computer == "p":
        print('user won')
        print(f"The user's input is {user}")
        print(f"The computer's input is {computer}")
        return
rock_paper_scisors()




