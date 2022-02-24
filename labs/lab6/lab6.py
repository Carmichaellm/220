"""
Name: Liam Carmichael
lab6.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import GraphWin, Text, Rectangle, Point, Entry

def vigenere():
    width = 600
    height = 600
    win = GraphWin("Vigenere", width, height)

    #message entry
    msg = Text(Point(200,100),"Message to code")
    msg.draw(win)
    msg_entry = Entry(Point(400,100), 20)
    msg_entry.draw(win)

    #keyword entry
    key_msg = Text(Point(200, 200), "Message to code")
    key_msg.draw(win)
    key_msg_entry = Entry(Point(400, 200), 20)
    key_msg_entry.draw(win)

    #encode button
    rect_button = Rectangle(Point(250,275), Point(350,325))
    rect_button.draw(win)
    button_txt = Text(Point(300,300),"Encode")
    button_txt.draw(win)
    win.getMouse()

    #cipher
    message = msg_entry.getText()
    message = message.replace(" ", "")
    message = message.upper()
    key = key_msg_entry.getText()
    key = key.replace(" ", "")
    key = key.upper()
    key_len = len(key)
    output_msg = ""
    for i in message:
        code = ord(i)
        code = code + key_len
        code = chr(code)
        output_msg = output_msg + code

    close_text = Text(Point(300,500), "Click Anywhere to Close Window")
    close_text.draw(win)
    button_txt.setText(output_msg)
    rect_button.setWidth(0)
    win.getMouse()
    win.close()

vigenere()