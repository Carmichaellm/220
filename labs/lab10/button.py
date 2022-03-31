from graphics import Rectangle, Text, GraphWin, Point

class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.label = Text(shape.getCenter(), label)

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    def draw(self, win):
        self.shape.draw(win)
        self.label.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.label.undraw()

    def is_clicked(self, point):
        x1 = self.shape.getP1().getX()
        y1 = self.shape.getP1().getY()
        x2 = self.shape.getP1().getX()
        y2 = self.shape.getP1().getY()
        xp = point.getX()
        yp = point.getX()
        if (x1 <= xp <= x2) and (y1 <= yp <= y2):
            return True
        if (x2 <= xp <= x1) and (y2 <= yp <= y1):
            return True
        return False

    def color_button(self, color):
        self.shape.setFill(color)