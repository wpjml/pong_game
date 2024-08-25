import turtle


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.dx = 3
        self.dy = 3

    def ball_move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def y_bounce(self):
        self.dy *= -1

    def x_bounce(self):
        self.dx *= -1

    def ball_reset_position(self):
        self.goto(0,0)
        self.x_bounce()
