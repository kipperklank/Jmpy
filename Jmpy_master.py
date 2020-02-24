
import turtle
go = turtle.Turtle()
turtle.Screen()
go.speed(0)
go.color('blue')
x=0.5
for i in range(10000):
   go.forward(x)
   x=x+0.5

   go.left(44)


turtle.done()
