from paddles import Paddle
from ball import Ball
from score import Score
from window import Window
import time

score = Score()
ball = Ball()
window = Window()

# creates two paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# creates a movement of the pressed key
window.root.listen()
window.root.onkey(right_paddle.move_up, "Up")
window.root.onkey(right_paddle.move_down, "Down")
window.root.onkey(left_paddle.move_up, "w")
window.root.onkey(left_paddle.move_down, "s")

# the entire game logic
is_on = True
while is_on:
    time.sleep(ball.ball_speed)
    window.root.update()
    ball.move()

    # collision of the ball with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_collapse()

    # collision of the ball with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320\
            or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_collapse()

    if ball.xcor() > 380:
        ball.new_round()
        score.left_player()

    if ball.xcor() < -380:
        ball.new_round()
        score.right_player()

window.root.exitonclick()
