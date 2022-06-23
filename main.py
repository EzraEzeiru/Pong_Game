from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
ball = Ball()
screen.tracer(0)


l_paddle = Paddle((-370, 0))
r_paddle = Paddle((370, 0))

l_score = Score((-100, 200))
r_score = Score((100, 200))

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
   time.sleep(ball.ball_speed)
   screen.update()
   ball.move()
   if ball.ycor() > 285 or ball.ycor() < -285:
       ball.bounce_y()

   if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
       ball.bounce_x()

   if ball.xcor() > 380:
       l_score.add_l_paddle()
       ball.reset_position()

   elif ball.xcor() < -380:
       r_score.add_r_paddle()
       ball.reset_position()

screen.exitonclick()