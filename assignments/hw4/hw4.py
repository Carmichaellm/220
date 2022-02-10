"""
Name: Liam Carmichael
hw4.py

Problem: Practice accumulating sequences.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Rectangle, GraphWin, Point, Text, Circle


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move circle")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(0,0),Point(50,50))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape.move(change_x, change_y)
        # shape2 = shape.clone(win)
        # shape2.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    width = 600
    height = 600
    win = GraphWin("Rectangle",width, height)
    message = Text(Point((width/2),(height/2)),"click to draw a square")
    message.draw(win)

    click_1 = win.getMouse()
    point_1 = Point(click_1.getX(), click_1.getY())
    click_2 = win.getMouse()
    point_2 = Point(click_2.getX(), click_2.getY())
    shape = Rectangle(point_1,point_2)
    shape.setFill("green")

    side_x = abs(click_1.getX() - click_2.getX())
    side_y = abs(click_1.getY() - click_2.getY())

    perimeter = (side_x * 2) + (side_y * 2)
    area = side_x * side_y

    perimeter_msg = Text(Point((width/2),(height-50)),"Perimeter:")
    perimeter_msg.setText("Perimeter:",perimeter)
    #area_msg =

    message.setText("click again to close")
    shape.draw(win)
    win.getMouse()
    win.close()


def circle():
    pass


def pi2():
    pass #what does approximating pi mean?


if __name__ == '__main__':
    pass
