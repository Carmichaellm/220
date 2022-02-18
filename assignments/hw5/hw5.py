"""
Name: Liam Carmichael
hw5.py

Problem: Index and slice strings and lists in python.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = input("enter a name (first last): ")
    name = name.split()
    print(name[1] + ",", name[0])


def company_name():
    domain = input("enter a domain: ")
    domain = domain.split(".")
    print(domain[1])


def initials():
    students = eval(input("how many students are in the class?"))
    for i in range(students):
        print("what is the name of student", i+1, end="")
        name = input("?")
        name = name.split()
        print(name[0][0] + name[1][0])


def names():
    names = input("enter a list of names: ")
    names = names.split(", ")
    for i in names:
        i = i.split()
        print(i[0][0] + i[1][0],end="\t")


def thirds():
    sentences = eval(input("enter the number of sentences: "))
    for i in range(sentences):
        print("enter sentence", i+1, end="")
        sent = input(":")
        print(sent[0:len(sent)+1:3])



def word_average():
    sentence = input("enter a sentence: ")
    sentence = sentence.split()
    average = 0
    for i in sentence:
        average = average + len(i)
    average = average / len(sentence)
    print(average)


def pig_latin():
    sentence = input("enter a sentence to convert to pig latin: ")
    sentence = sentence.lower()
    sentence = sentence.split()
    for i in sentence:
        i = i[1:len(i)+1] + i[0] + "ay"
        print(i,end=" ")


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
