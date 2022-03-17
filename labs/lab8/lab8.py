"""
Name: Liam Carmichael
lab8.py

Problem:  Create a programs that simulates bumber cars using the graphics package

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import GraphWin, Circle, color_rgb

def get_random(move_amount):
    movement = randint(-move_amount, move_amount)
    return movement
def did_collide(ball, ball2):
    if (ball.getX == ball2.getX) and (ball.getY == ball2.getY):
        return True
    return False
def hit_vertical(ball, win):
    min = 0
    max = win.getHeight()
    pos = ball.getY()
    if (pos == min) or (pos == max):
        return True
    return False
def hit_horizontal(ball, win):
    min = 0
    max = win.getWidth()
    pos = ball.getX()
    if (pos == min) or (pos == max):
        return True
    return False
def get_random_color():
    c_range = randint(0,255)
    random_color = color_rgb(c_range,c_range,c_range)
    return random_color

# if __name__ == '__main__':
#     ball
#     ball2
#     ball_xm
#     ball_ym
#     ball2_xm
#     ball2_ym
#     while True:
#         if ball