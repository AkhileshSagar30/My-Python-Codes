from turtle import Turtle,Screen,colormode
import random


def coloring():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

colormode(255)
directions = [0,90,180,270]

tom = Turtle()
tom.speed('fastest')

for i in range(360):
    tom.color(coloring())
    tom.circle(100)
    tom.setheading(5*i)

screen = Screen()
screen.exitonclick()
