"""
Name: Liam Carmichael
lab11.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from labs.lab10.door import Door
from labs.lab10.button import Button
from graphics import Rectangle, Text, GraphWin, Point
from random import randint

def main():
    #window
    win = GraphWin('Three Door Game',800,800)

    #door 1
    door_rect1 = Rectangle(Point(50,200),Point(250,600))
    door_text1 = Text(door_rect1.getCenter(), 'Door 1')
    door1 = Door(door_rect1,door_text1)
    door1.color_door('white')
    door1.draw(win)

    #door 2
    door_rect2 = door_rect1.clone()
    door_rect2.move(250,0)
    door_text2 = Text(door_rect2.getCenter(), 'Door 2')
    door2 = Door(door_rect2, door_text2)
    door2.color_door('white')
    door2.draw(win)

    #door 3
    door_rect3 = door_rect2.clone()
    door_rect3.move(250, 0)
    door_text3 = Text(door_rect3.getCenter(), 'Door 3')
    door3 = Door(door_rect3, door_text3)
    door3.color_door('white')
    door3.draw(win)

    #quit button
    butt_rect = Rectangle(Point(550,50),Point(750,150))
    butt_text = Text(butt_rect.getCenter(), 'Quit')
    button = Button(butt_rect,butt_text)
    button.draw(win)

    #wins
    wins_pts = 0
    wins_rect = Rectangle(Point(50,50),Point(150,150))
    wins_text = Text(wins_rect.getCenter(), wins_pts)
    wins = Button(wins_rect, wins_text)
    wins.draw(win)
    win_label = wins_text.clone()
    win_label.move(0,-60)
    win_label.setText('wins')
    win_label.draw(win)

    #losses
    loss_pts = 0
    loss_rect = Rectangle(Point(150,50),Point(250,150))
    loss_text = Text(loss_rect.getCenter(), loss_pts)
    loss = Button(loss_rect, loss_text)
    loss.draw(win)
    loss_label = loss_text.clone()
    loss_label.move(0, -60)
    loss_label.setText('losses')
    loss_label.draw(win)

    #top text
    top_text = Text(Point(400,175), 'I have a secret door')
    top_text.draw(win)

    #bottom text
    bot_text = Text(Point(400, 700), 'Click to guess which is the secret door!')
    bot_text.draw(win)

    #play
    while True:
        secret_door = randint(1, 3)
        if secret_door == 1:
            door1.set_secret(True)
            door2.set_secret(False)
            door3.set_secret(False)
        if secret_door == 2:
            door1.set_secret(False)
            door2.set_secret(True)
            door3.set_secret(False)
        if secret_door == 3:
            door1.set_secret(False)
            door2.set_secret(False)
            door3.set_secret(True)
        door1.color_door('white')
        door2.color_door('white')
        door3.color_door('white')
        top_text.setText('I have a secret door')
        bot_text.setText('Click to guess which is the secret door!')
        while True:
            click = win.getMouse()
            if door1.is_clicked(click):
                if door1.is_secret():
                    door1.color_door('green')
                    top_text.setText('you win')
                    bot_text.setText('click anywhere to play again')
                    wins_pts += 1
                    wins.set_label(wins_pts)
                    win.getMouse()
                    break
                else:
                    door1.color_door('red')
                    top_text.setText('sorry, incorrect!')
                    bot_text.setText('click anywhere to play again')
                    loss_pts += 1
                    loss.set_label(loss_pts)
                    win.getMouse()
                    break

            if door2.is_clicked(click):
                if door2.is_secret():
                    door2.color_door('green')
                    top_text.setText('you win')
                    bot_text.setText('click anywhere to play again')
                    wins_pts += 1
                    wins.set_label(wins_pts)
                    win.getMouse()
                    break
                else:
                    door2.color_door('red')
                    top_text.setText('sorry, incorrect!')
                    bot_text.setText('click anywhere to play again')
                    loss_pts += 1
                    loss.set_label(loss_pts)
                    win.getMouse()
                    break

            if door3.is_clicked(click):
                if door3.is_secret():
                    door3.color_door('green')
                    top_text.setText('you win')
                    bot_text.setText('click anywhere to play again')
                    wins_pts += 1
                    wins.set_label(wins_pts)
                    win.getMouse()
                    break
                else:
                    door3.color_door('red')
                    top_text.setText('sorry, incorrect!')
                    bot_text.setText('click anywhere to play again')
                    loss_pts += 1
                    loss.set_label(loss_pts)
                    win.getMouse()
                    break

            if button.is_clicked(click):
                win.close()

#run
main()
