
import turtle
window = turtle.Screen()
window.bgcolor("white")

turtle.penup
turtle.color("red")
turtle.fillcolor("red")
turtle.goto(-10, -5)
turtle.pendown()
turtle.begin_fill()
turtle.forward(70)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.end_fill()

turtle.penup()
turtle.goto(50, -25)
turtle.pendown()
turtle.color("black")
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.color("black")
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.color("red")
turtle.fillcolor("red")
turtle.goto(10, 15)
turtle.pendown()
turtle.begin_fill()
turtle.forward(30)
turtle.left(90)
turtle.forward(15)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(15)
turtle.left(90)
turtle.end_fill()

turtle.hideturtle()