"""
Name: Liam Carmichael
hw2.py

Problem: homework assignment 2

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper_bound = eval(input("what is the upper bound?"))
    threes = 0
    for i in range(0,upper_bound+1,3):
        threes = threes+i
    print("sum of threes is",threes)


def multiplication_table():
    number = 1
    for i in range(1,11):
        for j in range(1,11):
            number = i*j
            print(number,end="\t")
        print()



def triangle_area():
    a_length = eval(input("Enter side a length:"))
    b_length = eval(input("Enter side b length:"))
    c_length = eval(input("Enter side c length:"))
    letter_s = (a_length+b_length+c_length)/2
    area = math.sqrt(letter_s*(letter_s-a_length)*(letter_s-b_length)*(letter_s-c_length))
    print("area is",area)


def sum_squares():
    lower_range = eval(input("Enter the lower range:"))
    upper_range = eval(input("Enter the upper range:"))
    squares_sum = 0
    for i in range(lower_range,upper_range+1):
        squares_sum = squares_sum + (i*i)
    print(squares_sum)


def power():
    base = eval(input("Enter base:"))
    exponent = eval(input("Enter exponent:"))
    power_m = base
    for i in range(exponent-1):
        power_m = power_m*base
    print(base,"^",exponent,"=",power_m)


if __name__ == '__main__':
    pass
