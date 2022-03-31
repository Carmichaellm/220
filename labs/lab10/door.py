from graphics import Rectangle, Text, GraphWin, Point

class Door:
    def __init__(self, shape, label):
        self.shape = shape
        self.label = Text(shape.getCenter(), label)