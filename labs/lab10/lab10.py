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
    door_rect = Rectangle(Point(200,200),Point(400,600))
    door_text = Text(door_rect.getCenter(), 'closed')
    door = Door(door_rect,door_text)
    door.color_door('red')
    door.draw(win)
    butt_rect = Rectangle(Point(200,50),Point(400,150))
    butt_text = Text(butt_rect.getCenter(), 'exit')
    button = Button(butt_rect,butt_text)
    button.draw(win)
    #click = win.getMouse()
    while True:
        click = win.getMouse()
        #door.open('white', 'open')
        # if door.is_clicked(click):
        #     if door.get_label() == 'closed':
        #         door.open('white','open')
        #     if door.get_label() == 'open':
        #         door.close('red','closed')
        if door.is_clicked(click) and door.get_label() == 'closed':
            door.open('white', 'open')
        if door.is_clicked(click) and door.get_label() == 'open':
            door.close('red','closed')
        if button.is_clicked(click):
            win.close()


main()