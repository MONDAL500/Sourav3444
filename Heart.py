import turtle

t = turtle.Turtle()

t.goto(0,-10)

t.pensize(4)
t.color("red")
t.begin_fill()
t.left(146)
t.forward(155)
t.circle(-90,200)
t.setheading(55)
t.circle(-90,200)
t.forward(147)
t.end_fill()



t.goto(-130,125)
t.color("White")
t.write("Love you SONAI",font=("verdana",20,"bold"))
t.hideturtle()

turtle.done()