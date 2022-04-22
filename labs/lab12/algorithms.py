"""
Name: Liam Carmichael
algorithms.py

Problem: read numbers from a text file and output a list

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def read_data(filename):
    num_list = []
    num_file = open(filename, 'r')
    line = num_file.readline()
    while line != '':
        line_listed = line.split()
        count = 0
        while count < len(line_listed):
            num_list.append(int(line_listed[count]))
            count += 1
        line = num_file.readline()
    num_file.close()
    return num_list

def is_in_linear(search_val, values):
    limit = len(values)
    count = 0
    while count <= limit - 1:
        if values[count] == search_val:
            return True
        count += 1
    return False

def is_in_binary(search_val, values):
    left_index = 0
    right_index = len(values) - 1
    while left_index <= right_index:
        middle_index = (right_index + left_index) // 2
        middle_value = values[middle_index]
        if middle_value == search_val:
            #return middle_index
            return True
        elif middle_value < search_val:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
    #return -1
    return False

def selection_sort(values):
    temp_list = []
    list_len = len(values)
    while len(temp_list) < list_len:
        mini = values[0]
        for i in values:
            if i < mini:
                mini = i
        temp_list.append(mini)
        values.remove(mini)
    values = temp_list
    return values