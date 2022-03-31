"""
Name: Liam Carmichael
lab10.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from door import Door
from button import Button
from graphics import Rectangle, Text, GraphWin, Point

def main():
    win = GraphWin('test',600,600)
    door = Door(Rectangle(Point(200,200),Point(400,600)),'closed')
    door.color_door('red')
    door.draw(win)
    button = Button(Rectangle(Point(200,50),Point(400,150)),'exit')
    button.draw(win)
    click = win.getMouse()
    while not button.is_clicked(click):
        door.open('white', 'open')
        if door.is_clicked(click):
            if door.get_label() == 'closed':
                door.open('white','open')
            if door.get_label() == 'open':
                door.close('red','closed')
        click = win.getMouse()
        button.is_clicked(click)

main()