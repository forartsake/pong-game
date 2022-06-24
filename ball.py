from turtle import Turtle


class Ball(Turtle):
    """The class that creates a ball."""
    def __init__(self):
        Turtle.__init__(self)
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('white')
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.ball_speed = 0.05

    def move(self):
        """ The ball moves by increasing 5px on x and y coordinates"""
        x_coordinate = self.xcor() + self.x_move
        y_coordinate = self.ycor() + self.y_move
        self.goto(x_coordinate, y_coordinate)

    def wall_collapse(self):
        """The ball reverses direction when it hits a wall"""
        self.y_move *= -1

    def paddle_collapse(self):
        """The ball reverses direction when it hits a paddle with increasing speed"""
        self.x_move *= -1
        self.ball_speed *= 0.9

    def new_round(self):
        """Returns a ball to the center with reverse direction"""
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.paddle_collapse()
