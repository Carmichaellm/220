"""
Name: Liam Carmichael
hw6.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def cash_converter():
    integer = eval(input("enter an integer: "))
    integer = float(integer)
    integer = round(integer,2)
    cash = "That is ${}0".format(integer)
    print(cash)


def encode():
    message = input("enter a message: ")
    key = eval(input("enter a key: "))
    for i in message:
        code = ord(i)
        code = code + key
        code = chr(code)
        print(code,end="")


def sphere_area(radius):
    area = 4 * math.pi * (radius ** 2)
    return area


def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    volume = int(volume)
    print(volume)


def sum_n(number):
    sumn = 0
    for i in range(number+1):
        sumn = sumn + i
    return sumn


def sum_n_cubes(number):
    pass #what is a cube of a natural number?


def encode_better():
    pass


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
