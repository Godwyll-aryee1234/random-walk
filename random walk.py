from turtle import Turtle, Screen
from random import choice

import randomcolor

t = Turtle()
s = Screen()
t.pensize(5)
t.hideturtle()
t.speed(4)
i = 1
while i <= 1000:
    directions = [0, 90, 180, 270]
    t.color(randomcolor.RandomColor().generate())
    t.setheading(choice(directions))
    t.forward(20)
    i += 1

s.exitonclick()