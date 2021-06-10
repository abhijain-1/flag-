import turtle

def flag(color):
    f.begin_fill()
    f.fillcolor(color)
    
    for i in range(2):
      
      f.rt(90)
      f.fd(400)
      f.rt(90)
      f.fd(100)
    f.end_fill()
      
f=turtle.Turtle()

f.up()
f.goto(0,-400)
f.down()
f.goto(0,400)
f.lt(90)
flag("orange")
f.up()
f.goto(0,300)
f.down()
flag("white")
f.up()
f.goto(0,200)
f.down()
flag("green")
f.up()
f.goto(250,250)
f.down()
f.begin_fill()
f.fillcolor("blue")
f.circle(50)
f.hideturtle()





