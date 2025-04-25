import turtle
#start
t = turtle.Turtle()
t.speed(100000)
t.penup()

t.goto(100, 0)
t.pendown()
t.color("red")

for i in range(100):
    t.forward(100)
    t.left(73)

t.penup()

t.goto(135, -50)
t.pendown()


t.color("green")

for i in range(100):
    t.forward(100)
    t.left(73)
# middle
t.penup()
t.goto(0, 150)
t.pendown()
t.color("black")
for i in range(100):
    t.forward(100)
    t.left(73)

t.penup()
t.goto(-190 , -10)
t.pendown()
t.color("yellow")
for i in range(100):
    t.forward(100)
    t.left(73)

t.penup()
t.goto(-190, -20)
t.pendown()
t.color("blue")
for i in range(100):
    t.forward(100)
    t.left(73)
t.penup()
#end
turtle.exitonclick()