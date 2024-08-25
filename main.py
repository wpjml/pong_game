import time
import turtle
import paddle
import ball
import score_board

screen = turtle.Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = paddle.Paddle(350, 0)
l_paddle = paddle.Paddle(-350, 0)


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = ball.Ball()
score_board = score_board.Scoreboard()
mannnaka = turtle.Turtle()
mannnaka.setheading(90)
mannnaka.color("white")
mannnaka.penup()
mannnaka.goto(0 , -300)
mannnaka.hideturtle()
mannnaka.pendown()
for _ in range(30):
    mannnaka.forward(10)
    mannnaka.penup()
    mannnaka.forward(10)
    mannnaka.pendown()


is_game_on = True
while is_game_on:
    screen.update()
    ball.ball_move()

    if 280 < ball.ycor() or -280 > ball.ycor():
        ball.y_bounce()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340 or
            ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.x_bounce()

    if 380 < ball.xcor():
        ball.ball_reset_position()
        time.sleep(3)
        score_board.l_point()

    if -380 > ball.xcor():
        ball.ball_reset_position()
        time.sleep(3)
        score_board.r_point()


screen.exitonclick()
