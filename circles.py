import turtle
import random

turtle.speed(0)
turtle.pensize(4)
turtle.bgcolor("black")

def colorpicker():
    c = ['red','orange','yellow','green','blue','indigo','violet']
    colorr = random.randrange(0,6)
    return c[colorr]

for i in range (80):
    turtle.circle(150)
    turtle.color(colorpicker())
    turtle.right(25)