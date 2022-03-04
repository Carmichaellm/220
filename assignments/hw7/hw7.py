"""
Name: Liam Carmichael
hw7.py

Problem: reading and writing text files

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def number_words(in_file_name, out_file_name):
    with open(in_file_name) as read:
        text = read.read()
    with open(out_file_name, 'w') as write:
        order = 0
        sep_wor = text.split()
        for i in range(len(sep_wor)):
            order = order + 1
            out = str(order) + " " + sep_wor
            write.write(out)
            write.write('\n')





def hourly_wages(in_file_name, out_file_name):
    with open(in_file_name) as read:
        text = read.readlines()
    with open(out_file_name, 'w') as write:
        for i in text:
            line = i.split()
            wage = int(line[2]) + 1.65
            pay = wage * line[3]
            pay = round(pay, 2)
            out = line[0] + " " + line[1] + " " + str(pay)
            write.write(out)
            write.write('\n')


def calc_check_sum(isbn):
    isbn = isbn.replace('-', '')
    order = 10
    for i in range(len(isbn)+1):
        prod = int(isbn[i]) * order
        sum = sum + prod
        order = order - 1
    return sum



def send_message(file_name, friend_name):
    with open(file_name) as read:
        text = read.read()
    with open(friend_name, 'w') as write:
        write.write(text)


def encode():
    pass


def send_safe_message(file_name, friend_name, key):
    pass


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass


if __name__ == '__main__':
    pass
