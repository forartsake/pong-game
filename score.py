from turtle import Turtle

class Score(Turtle):
    """This class creates a scoreboard"""
    def __init__(self):
        Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.color('white')
        self.left_player_score = 0
        self.right_player_score = 0
        self.score_update()


    def score_update(self):
        """Updates the scoreboard"""
        self.clear()
        self.goto(-50, 200)
        self.write(self.left_player_score, font=("Times New Roman", 48, "bold"), align="left")
        self.goto(0, 200)
        self.write(":",font=("Times New Roman", 60, "bold"), align="center")
        self.goto(50, 200)
        self.write(self.right_player_score, font=("Times New Roman", 48, "bold"), align="right")

    def left_player(self):
        """Gives a point to the left player"""
        self.left_player_score += 1
        self.score_update()

    def right_player(self):
        """Gives a point to the right player"""
        self.right_player_score += 1
        self.score_update()

