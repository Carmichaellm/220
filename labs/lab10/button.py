from graphics import Rectangle, Text, GraphWin, Point

class Button:
    def __init__(self, shape, text):
        self.shape = shape
        self.text = text

    def get_label(self):
        return self.text.getText()

    def set_label(self, text):
        self.text.setText(text)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        x1 = self.shape.getP1().getX()
        y1 = self.shape.getP1().getY()
        x2 = self.shape.getP2().getX()
        y2 = self.shape.getP2().getY()
        xp = point.getX()
        yp = point.getY()
        if (x1 <= xp <= x2) and (y1 <= yp <= y2):
            return True
        if (x2 <= xp <= x1) and (y2 <= yp <= y1):
            return True
        return False

    def color_button(self, color):
        self.shape.setFill(color)