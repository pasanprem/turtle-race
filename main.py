from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=400)

race_on = True
choice = screen.textinput("Make your choice", "What is the color you choose?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(x=-380, y=(-100) + turtle_index * 50)
    all_turtles.append(t)

while race_on:
    for _ in all_turtles:
        dist = random.randint(1, 10)
        _.forward((dist))

screen.exitonclick()
