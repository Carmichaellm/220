from graphics import Circle, Line, Polygon


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        self.mouth.undraw()
        triangle = Polygon(self.mouth.getP1(), self.mouth.getP2(), self.mouth.getCenter())
        triangle.draw(self.window)

    def shock(self):
        self.mouth.undraw()
        new_mouth = Circle(self.mouth.getCenter(), self.right_eye.getRadius())
        new_mouth.draw(self.window)

    def wink(self):
        self.mouth.undraw()
        triangle = Polygon(self.mouth.getP1(), self.mouth.getP2(), self.mouth.getCenter())
        triangle.draw(self.window)
        self.right_eye.undraw() #my right or his right?
        nep1 = self.right_eye.getCenter()
        nep1.move(-self.right_eye.getRadius(), 0)
        nep2 = self.right_eye.getCenter()
        nep2.move(self.right_eye.getRadius())
        new_eye = Line(nep1, nep2)
        new_eye.draw(self.window)
