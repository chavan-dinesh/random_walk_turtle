import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# colors = ["orange red", "navajo white", "peru", "gold", "medium violet red", "blue violet", "gray", "green", "black", "light sky blue"]
direction = [0, 90, 180, 270]

def random_walk():
    tim.pensize(15)
    tim.speed('fastest')
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))

for _ in range(500):
    random_walk()

screen = Screen()
screen.exitonclick()

