"""
Name: Liam Carmichael
hw1.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the players's total shots: "))
    shots_made = eval(input("Enter how many shots the player made: "))
    shooting_percentage = shots_made/total_shots
    print("Shooting Percentage:",shooting_percentage,"%")


def coffee():
    coffee_pounds = eval(input("How many pounds of coffee would you like?"))
    total = (10.5+0.86)*coffee_pounds+1.50
    print("You're total is:",total)


def kilometers_to_miles():
    kilometers = (eval(input("How many kilometers did you travel?")))
    miles = kilometers*0.6213371
    print("That's",miles,"miles!")


if __name__ == '__main__':
    pass
