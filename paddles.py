from turtle import Turtle


class Paddle(Turtle):
    """Class that creates paddle."""
    def __init__(self, coordinates):
        Turtle.__init__(self)
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('#C71585')
        self.penup()
        self.goto(coordinates)

    def move_up(self):
        """Moves a paddle 20 px up."""
        y_coordinate = self.ycor() + 20
        self.goto(self.xcor(), y_coordinate)

    def move_down(self):
        """Moves a paddle 20 px down."""
        y_coordinate = self.ycor() - 20
        self.goto(self.xcor(), y_coordinate)
