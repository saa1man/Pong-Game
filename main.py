from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# window settings
screen=Screen()
screen.setup(800,600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(0)
# creatimh scoreboard.
scoreboard=Scoreboard()
# creating paddles
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
# creating ball
ball=Ball()
# animation
screen.listen()
    #for right paddle:
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
    #for left paddle:
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

# running game
is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # collision with wall.
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    # collision with paddle.
    if ball.distance(r_paddle)<60 and ball.xcor()>320 or ball.distance(l_paddle)<60 and ball.xcor()<-320:
        ball.bounce_x()
    # missing right paddle.
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
    # missing left paddle.
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
        
screen.exitonclick()