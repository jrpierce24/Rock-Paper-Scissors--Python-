import random

win_counter = 0
lose_counter = 0
new = 0
comp_num = 0

def game():
    global win_counter
    global lose_counter
    global comp_num

    while win_counter < 2 or lose_counter < 2:
        display()
        read()
        comp_num = random.randint(1, 3)
        print(comp_num)
        if compare() == 2:
            print("You Win!")
            win_counter += 1
        if compare() == 1:
            print("Computer Wins!")
            lose_counter += 1
        elif compare() == 3:
            print("Draw")



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


game()
