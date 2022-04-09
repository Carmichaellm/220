"""
Name: Liam Carmichael
hw10.py

Problem:

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def fibonacci(n):
    count = 0
    fib = 1
    fib_seq = [1]
    if n < 1:
        return None
    else:
        while count + 1 < n:
            fib_seq.append(fib)
            fib_old = fib_seq[count]
            fib = fib + fib_old
            count += 1
    fib_seq.reverse()
    return fib_seq[0]


def double_investment(principle, rate):
    year = 0
    total = principle
    while total < principle * 2:
        total = total * (1 + rate)
        year += 1
    return year


def syracuse(n):
    syr_list = [n]
    while syr_list[len(syr_list)-1] > 1:
        if syr_list[len(syr_list)-1] % 2 == 0:
            syr_list.append(int(syr_list[len(syr_list)-1] / 2))
        else:
            syr_list.append(int((3 * syr_list[len(syr_list)-1]) + 1))
    return syr_list