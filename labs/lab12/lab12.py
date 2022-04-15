"""
Name: Liam Carmichael
lab10.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from algorithms import read_data, is_in_linear
from random import randint

def find_and_remove_first(_list, value):
    x = _list.index(value)
    _list.insert(x, 'liam')
    x = _list.index(value)
    _list.pop(x)
    #_list.remove(value)

def good_input():
    range_check = eval(input('input a number 1 to 10'))
    while (range_check < 1) or (range_check > 10):
        range_check = eval(input('input a number 1 to 10'))
    return range_check

def num_digits():
    num = eval(input('input a positive integer'))
    while num > 0:
        num_out = int(num)
        digits = 0
        while num_out > 0:
            num_out = num_out//10
            digits += 1
        print(digits)
        num = eval(input('input a positive integer'))

def hi_lo_game():
    sec_num = randint(1,100)
    guess = 0
    while guess < 7:
        ges_num = eval(input('guess a number 1 to 100'))
        guess += 1
        if ges_num > sec_num:
            print("too high")
        if ges_num < sec_num:
            print("too low")
        if ges_num == sec_num:
            print("You win in {} guesses!".format(guess))
            break
    if guess >= 7:
        print("Sorry, you lose. The number was {}".format(sec_num))


def main():
    print(find_and_remove_first([1,2,3], 3))
    values = read_data('data_sorted.txt')
    print(is_in_linear(0, values[0]))
    good_input()
    num_digits()
    hi_lo_game()