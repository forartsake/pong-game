from turtle import Screen

image = "images/bg.gif"


class Window:
    """This class creates a window"""
    def __init__(self):
        self.root = Screen()
        self.root.title("Pong Game")
        self.root.setup(width=800, height=600)
        self.root.bgpic(image)
        self.root.tracer(0)




