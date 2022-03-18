"""
Name: Liam Carmichael
hw8.py

Problem:

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        if type(nums[i]) == type(1):
            nums[i] = nums[i] * nums[i]
            nums[i] = int(nums[i])
        if type(nums[i]) == type(1.0):
            nums[i] = nums[i] * nums[i]
            nums[i] = float(nums[i])



def sum_list(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc



def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])


def sum_of_squares(nums): #output matches expected but test claims its wrong
    for i in range(len(nums)):
        split = nums[i].split(',')
        acc = 0
        for j in range(len(split)):
            split[j] = float(split[j])
            split[j] = split[j] * split[j]
            acc = acc + split[j]
        nums[i] = acc


def starter(weight, wins):
    if ((weight >= 150) and (weight < 160)) and (wins >= 5):
        return True
    if (weight > 199) or (wins > 19):
        return True
    return False


def leap_year(year):
    if (year % 4 == 0) and not (year % 100 == 0):
        return True
    if (year % 400 == 0):
        return True
    return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    pass


if __name__ == '__main__':
    pass
