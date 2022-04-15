"""
Name: Liam Carmichael
algorithms.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def read_data(filename):
    num_list = []
    num_file = open(filename, 'r')
    line = num_file.readline()
    while line != '':
        num_list.append(line)
        line = num_file.readline()
    return num_list

def is_in_linear(search_val, values):
    limit = len(values)
    count = 0
    while count <= limit - 1:
        if values[count] == search_val:
            return True
        count += 1
    return False