import random

win_counter = 0
lose_counter = 0
new = 0
comp_num = 0


def game():
    global win_counter
    global lose_counter
    global comp_num
    win_counter = 0
    lose_counter = 0
    space(4)

    while True:

        display()

        space(3)

        read()

        comp_num = random.randint(1, 3)
        computer(comp_num)

        space(1)
        if compare() == 2:
            print("You Win!")
            win_counter += 1
        if compare() == 1:
            print("Computer Wins!")
            lose_counter += 1
        elif compare() == 3:
            print("Draw")
        pause()
        if check_wins() == 1 or check_wins() == 0:
            print("Win Count: " + str(win_counter) + " " "Lose Count: " + str(lose_counter))
            break

    space(2)
    play_again()


def display():
    print("Win Count: " + str(win_counter) + " " "Lose Count: " + str(lose_counter))
    print("Rock, Paper, Scissors....")


def read():
    global new
    good_data = False

    while not good_data:
        user_input = input()
        # Checks Input
        new = check(user_input)

        if new == 0:
            print("Please Re-enter your attack!")
        elif new == 1 or new == 2 or new == 3:
            good_data = True


def check(data):
    if data == "Rock" or data == "rock" or data == "r" or data == "R":
        return 1
    elif data == "Paper" or data == "paper" or data == "p" or data == "P":
        return 2
    elif data == "Scissors" or data == "Scissors" or data == "s" or data == "S":
        return 3

    return 0


def compare():
    if comp_num == new:
        return 3

    elif comp_num == 1 and new == 3:
        return 1

    elif comp_num == 3 and new == 2:
        return 1

    elif comp_num == 2 and new == 1:
        return 1

    elif comp_num == 3 and new == 1:
        return 2

    elif comp_num == 2 and new == 3:
        return 2

    elif comp_num == 1 and new == 2:
        return 2


def computer(selection):
    print("VS")
    if selection == 1:
        print("Rock")
    if selection == 2:
        print("Paper")
    if selection == 3:
        print("Scissors")


def check_wins():
    if win_counter == 2:
        return 1
    elif lose_counter == 2:
        return 0


def space(x):
    if x == 1:
        print(" ")
    if x == 2:
        for x in range(20): print(" ");
    if x == 3:
        print("")
        print("")
    if x == 4:
        for x in range(45): print(" ")


def pause():
    space(1)
    input("Press Enter to Continue....")

def play_again():
    aws = input("Would you like to play again you fool?  : ")
    if aws == "yes" or aws == "Yes" or aws == "Y" or aws == "y":
        game()


game()