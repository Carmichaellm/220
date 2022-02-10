from graphics import GraphWin, Point, Circle, Polygon, Text, Line
from time import sleep

def greeting_card():
    #window
    win = GraphWin("greeting card",600,600)
    background_color = "blue"
    win.setBackground(background_color)

    #adjust heart with these variables
    heart_pos = 300
    heart_height = 300
    radius = 50
    heart_color = "red"

    #left heart parts
    left_heart_point = Point(heart_pos - radius, heart_height)
    left_heart = Circle(left_heart_point,radius)
    left_heart.setFill(heart_color)
    left_heart.setOutline(background_color)

    #right heart part
    right_heart_point = Point(heart_pos + radius, heart_height)
    right_heart = Circle(right_heart_point,radius)
    right_heart.setFill(heart_color)
    right_heart.setOutline(background_color)

    #bottom heart part
    bottom_heart_left = Point(heart_pos-(radius*2),heart_height)
    bottom_heart_right = Point(heart_pos+(radius*2),heart_height)
    bottom_heart_point = Point(heart_pos,heart_height+200)
    bottom_heart = Polygon(bottom_heart_left, bottom_heart_right, bottom_heart_point)
    bottom_heart.setFill(heart_color)
    bottom_heart.setOutline(heart_color)

    #heart draw
    left_heart.draw(win)
    right_heart.draw(win)
    bottom_heart.draw(win)

    #greeting message
    vd_msg_pnt = bottom_heart_point.clone()
    vd_msg_pnt.move(0,25)
    vd_msg = Text(vd_msg_pnt,"Happy Valentine's Day!")
    vd_msg.draw(win)

    #arrow
    arrow_x = 600
    arrow_y = 0
    arrow_color = "white"
    spine_up = Point(arrow_x,arrow_y)
    spine_dn = Point(arrow_x+100,arrow_y-100)
    spine = Line(spine_up,spine_dn)
    bullet = Polygon(spine_up, Point(arrow_x+25,arrow_y), Point(arrow_x,arrow_y-25))
    bullet.setFill(arrow_color)
    fletch = Polygon(spine_dn, Point(arrow_x+125,arrow_y-100), Point(arrow_x+100,arrow_y-125))
    fletch.setFill(arrow_color)
    spine.draw(win)
    bullet.draw(win)
    fletch.draw(win)

    #annimation
    for i in range(300):
        spine.move(-1,1)
        bullet.move(-1,1)
        fletch.move(-1,1)

    closing_msg = Text(Point(300,100),"Click anywhere to close")
    closing_msg.draw(win)
    win.getMouse()
    win.close()