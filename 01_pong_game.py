import turtle
import os 
from playsound import playsound
import winsound


# creating a window for the pong game
wn = turtle.Screen()
wn.title("2 player pong game")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)
# tracer speeds up the game and prevents the window from getting updated and we have to manually update the window


#score
score_a=0
score_b=0

#paddle A
#capital t turtle is class name and small t turtle is the module name as impoted above
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-350,0)


#paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
b=turtle.Turtle()
b.speed(0)
b.shape("circle")
b.color("white")
b.penup()
b.goto(0,0)
# now we gotta focus on the balls movement
b.dx = 0.06
b.dy = -0.06

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0    Player B: 0",align="center",font=("Courier",22,"normal"))


# functions for moving paddle up and paddle down 
def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -=10
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y +=10
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -=20
    paddle_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


# main game loop
while True:
    wn.update()


    #move the ball
    x, y = b.position()
    b.setposition(x + b.dx, y + b.dy)

    #border checking ie ball will react when it reaches end of screen
    if b.ycor() > 290:
        b.sety(290)
        b.dy *= -1
        # playsound('C:\\Users\\91700\\Desktop\\python\\game')
        # os.system("afplay bouunce.wav&")
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if b.ycor() < -290:
        b.sety(-290)
        b.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if b.xcor()>390:
        b.goto(0,0)
        b.dx *= -1 
        score_a +=1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a,score_b),align="center",font=("Courier",22,"normal"))


    if b.xcor() < -390:
        b.goto(0,0)
        b.dx *= -1 
        score_b +=1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a,score_b),align="center",font=("Courier",22,"normal"))
   

    # paddle and ball collisions
    if (b.xcor() >345 and b.xcor() < 350) and (b.ycor() < paddle_b.ycor() + 40 and b.ycor() > paddle_b.ycor() - 40):
        b.setx(345)  
        b.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if (b.xcor() < -345 and b.xcor() > -350) and (b.ycor() < paddle_a.ycor() + 40 and b.ycor() > paddle_a.ycor() - 40):
        b.setx(-345)  
        b.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)  