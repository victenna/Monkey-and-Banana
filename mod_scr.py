#mod_scr
import turtle,time
score=turtle.Turtle()
score.hideturtle()
score.up()
score.color('blue')
s=0
FONT=('Times New Roman', 20, 'bold')
t_num='Total number of shotts='
def scr():
    global s
    s=s+1
    time.sleep(0.5)
    score.goto(50,-50)
    score.clear()
    score.write ('Score=', font =FONT)
    score.goto(135,-50)
    score.write (s,font=FONT)
   
total=turtle.Turtle()
total.hideturtle()
total.up()
total.color('blue')
r=0
def tot_number():
    global r
    r=r+1
    #time.sleep(0.5)#!!!!!!
    total.goto(-100,0)
    total.clear()           
    total.write (t_num, font=FONT)
    total.goto(330,0)
    total.write (r, font=FONT)

