"""
Name: Liam Carmichael
hw3.py

Problem: Develop simple Python programs that do input, produce output and do arithmetic using loops.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def average():
    grade_entries = eval(input("how many grades will you enter? "))
    grade_values = 0
    for i in range(grade_entries):
        grade_scores = eval(input("Enter grade: "))
        grade_values = grade_values + grade_scores
    grade_values = grade_values / grade_entries
    print("average is",grade_values)


def tip_jar():
    tip_total = 0
    for i in range(5):
        tip = eval(input("how much would you like to donate? "))
        tip_total = tip_total + tip
    print("total tips:", tip_total)



def newton():
    target = eval(input("What number do you want to square root? "))
    times =  eval(input("How many times should we improve the approximation? "))
    approx = target
    for i in range(times):
        approx = ((approx + (target / approx)) / 2)
    print("the square root is approximately", approx)
    #what the heck is an approx?



def sequence():
    # terms = eval(input("how many terms would you like? "))
    # seq = 0
    # for i in range(terms):
    #     print(seq,seq,end="\t")
    #     seq = seq + 2
    #never seen any math remotely like this, no idea where to even begin



def pi():
    pass
#this math is totally alien to me


if __name__ == '__main__':
    pass
