import turtle,random,math
import time
from mod_scr import *
import winsound # Import sound library
wn=turtle.Screen()
wn.setup(800,500)
wn.bgpic('monkeytree3.gif')
turtle.tracer(2)
t=turtle.Turtle()
t.hideturtle()
t.up()
t.begin_poly()
t.fd(280)
t.left(90)
t.fd(1)
t.left(90)
t.fd(280)
t.fd(1)
t.end_poly()
wn.addshape('tire',t.get_poly())
t=turtle.Turtle(shape='tire')
t.hideturtle()
t.tilt(90)
t.up()
t.goto(0,200)  
t.lt(180)
t.color('green')
t.showturtle()
image='monk.gif'
wn.addshape(image)
monkey=turtle.Turtle()
monkey.shape(image)
monkey.up()
monkey.hideturtle()
monkey.goto(-268,125) 
monkey.showturtle()
monkey.setheading(-90)

wn.addshape('banana.gif')
banana=turtle.Turtle()
banana.shape('banana.gif')
banana.up()
#banana.hideturtle()
#banana.showturtle()
banana.setheading(-90)

X=400
Y=400
def left():
    global X
    global Y
    t.rt(5)
    angle=t.heading()-180
    angle1=round(angle/5)
    monkey.circle(280,-5)
    X,Y=monkey.position()
    
def right():
    global X
    global Y
    t.rt(-5)
    angle=t.heading()-180
    angle1=round(angle/5)
    monkey.circle(280,5)
    X,Y=monkey.position()
wn.listen()
wn.onkey(left,'Left')
wn.onkey(right,'Right')
   
while True:
    banana.goto(random.randint(-200,200),300)
    banana.showturtle()
    
    for i in range(360*8):
        banana.fd(0.25)
        X1,Y1=banana.position()
        delta=abs(math.sqrt((X-X1)**2+(Y-Y1)**2))
        if delta<40:
            banana.hideturtle()
            banana.goto(500,500)
            frequency=1000 #Sound
            duration=100  # Sound
            winsound.Beep(frequency,duration) # Sound
            scr()
    
    banana.hideturtle()
