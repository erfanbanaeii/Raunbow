import turtle

colors = ["red","yellow","blue","green","orange","purple"]

t = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 10)
    t.forward(x)
    t.left(59)