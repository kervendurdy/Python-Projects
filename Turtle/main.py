#
# @kervendurdy
#

import turtle
import random
def draw_petal(turtle, size):
    turtle.circle(size, 60)
    turtle.left(120)
    turtle.circle(size, 60)
    turtle.left(120)

def draw_flower(turtle, size):
    for _ in range(6):
        draw_petal(turtle, size)
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        turtle.color(r,g,b)
        draw_petal(turtle, size)
        turtle.left(60)

turtle.colormode(255)
flower = turtle.Turtle()
flower.speed(0)
turtle.bgcolor("black")
size = 300

while True:
    draw_flower(flower, size)
    size +=5
    flower.right(5)

turtle.done()


