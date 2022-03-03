"""
Name: Liam Carmichael
lab7.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def weighted_average(in_file_name, out_file_name):
    with open(in_file_name) as read:
        line = read.readlines()
    with open(out_file_name, 'w') as write:
        for i in range(len(line)):
            #student = line[i].split()
            nnn = line[i].split(":")
            numbers = nnn[1].split()
            weight = numbers[0:len(numbers):2]
            grade = numbers[1:len(numbers)+1:2]
            average = 0
            for j in range(len(grade)):
                average = average + (int(weight[j]) * int(grade[j]))
            average = average/100
            out_line = nnn[0][0:len(nnn[0])] + "'s average: " + str(average)
            write.write(out_line)
            write.write('\n')

def main():
    weighted_average("grades.txt", "avg.txt")

main()