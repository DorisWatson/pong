import turtle

import tkinter

# import tcl

import winsound



wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
#tracer(0) stops the window from automatically updating - game runs faster. 
#must update manually

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = -0.5

# Creating the scoreboard - Pen

pen = turtle.Turtle()
pen.speed()
pen.color("white")
pen.penup()
pen.hideturtle ()
pen.goto(0, 260)
pen.write ("Player A: 0   Player B 0", align="center", font=("Courier", 24, "normal"))

# Keeping score
score_a = 0
score_b = 0




#Function

def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)


#Keybord binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")

wn.listen()
wn.onkeypress(paddle_a_down, "s")

wn.listen()
wn.onkeypress(paddle_b_up, "Up")

wn.listen()
wn.onkeypress(paddle_b_down, "Down")


#Main game loop

while True:
    wn.update()

    #Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Boarder 
    # compare ball y coordinates

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        winsound.PlaySound("smb_coin", winsound.SND_ASYNC)
        pen.clear()
        pen.write ("Player A: {}   Player B {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        winsound.PlaySound("smb_coin", winsound.SND_ASYNC)
        pen.clear()
        pen.write ("Player A: {}   Player B {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


# Collision with paddle

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
       ball.setx(340)
       winsound.PlaySound("smb_jump", winsound.SND_ASYNC) 
       ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
       ball.setx(-340) 
       winsound.PlaySound("smb_jump", winsound.SND_ASYNC)
       ball.dx *= -1







