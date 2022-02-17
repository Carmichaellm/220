"""
Name: Liam Carmichael
lab5.py

Problem: Use python graphics and strings.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Polygon, Text, Point, Circle, Entry, color_rgb
from math import sqrt

def triange():
    width = 600
    height = 600
    win = GraphWin("Triangle", width, height)
    message = Text(Point((width / 2), (height / 2)), "click to draw a triangle")
    message.draw(win)

    click_1 = win.getMouse()
    point_1 = Point(click_1.getX(), click_1.getY())
    click_2 = win.getMouse()
    point_2 = Point(click_2.getX(), click_2.getY())
    click_3 = win.getMouse()
    point_3 = Point(click_3.getX(), click_3.getY())
    shape = Polygon(point_1, point_2, point_3)

    side_x = abs(click_1.getX() - click_2.getX())
    side_y = abs(click_1.getY() - click_2.getY())
    distance = sqrt(((click_2.getX() - click_1.getX()) ** 2) + ((click_2.getY() - click_1.getY()) ** 2))

    perimeter = side_x + side_y + distance
    lets = perimeter / 2
    area = sqrt(lets * (lets - side_x) * (lets - side_y) * (lets - distance))

    perimeter = str(perimeter)
    perimeter_text = "Perimeter: "
    perimeter_text = perimeter_text + perimeter
    perimeter_msg = Text(Point((width / 2), (height - 50)), perimeter_text)
    area = str(area)
    area_text = "Area: "
    area_text = area_text + area
    area_msg = Text(Point((width / 2), (height - 25)), area_text)

    area_msg.draw(win)
    perimeter_msg.draw(win)
    message.setText("click again to close")
    shape.draw(win)
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_text.draw(win)
    red_entry = Entry(Point(win_width / 2, win_height / 2 + 40),5)
    red_entry.draw(win)
    win.getMouse()
    red_value = red_entry.getText()
    red_value = int(red_value)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_text.draw(win)
    green_entry = Entry(Point(win_width / 2, win_height / 2 + 70), 5)
    green_entry.draw(win)
    win.getMouse()
    green_value = green_entry.getText()
    green_value = int(green_value)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_text.draw(win)
    blue_entry = Entry(Point(win_width / 2, win_height / 2 + 100), 5)
    blue_entry.draw(win)
    win.getMouse()
    blue_value = blue_entry.getText()
    blue_value = int(blue_value)

    #set circle color
    shape.setFill(color_rgb(red_value,green_value,blue_value))

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    sting = input("enter a string: ")
    print(sting[0])
    print(sting[-1])
    print(sting[2:6])
    print(sting[0] + sting[-1])
    for i in range(10):
        print(sting[0:3],end="")
    print(end="\n")
    for j in sting:
        print(j)
    print(len(sting))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)

def another_series():
    pass


def target():
    width = 600
    height = 600
    win = GraphWin("Target", width, height)

    center = Point(width/2, height/2)

    white = Circle(center,250)
    white.setFill('white')
    white.setOutline('white')
    white.draw(win)

    black = Circle(center, 200)
    black.setFill('black')
    black.setOutline('black')
    black.draw(win)

    blue = Circle(center, 150)
    blue.setFill('blue')
    blue.setOutline('blue')
    blue.draw(win)

    red = Circle(center, 100)
    red.setFill('red')
    red.setOutline('red')
    red.draw(win)

    yellow = Circle(center, 50)
    yellow.setFill('yellow')
    yellow.setOutline('yellow')
    yellow.draw(win)

    message = Text(Point((width / 2), height-25), "click to close")
    message.draw(win)
    win.getMouse()
    win.close()