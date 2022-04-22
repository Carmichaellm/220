"""
Name: Liam Carmichael
lab13.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from labs.lab12.algorithms import is_in_binary, selection_sort, read_data

def star_find(filename): #let it run a minute
    values = read_data(filename)
    values = selection_sort(values)
    count = 0
    pulse = []
    searched = 0
    for i in range(4000,5001):
        searched += 1
        if is_in_binary(i, values):
            count += 1
            pulse.append(i)
        if count == 5:
            break
    print('pulses found: {}'.format(count))
    print('pulse strength: {}'.format(pulse))
    print('pulses searched: {}'.format(searched))

def main():
    values = read_data('trades.txt')
    values = selection_sort(values)
    tes_val = is_in_binary(348, values)
    print(tes_val)

    star_find('signals.txt')