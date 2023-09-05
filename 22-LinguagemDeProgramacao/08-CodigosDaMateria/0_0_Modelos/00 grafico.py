import turtle
import math
import colorsys

turtle.setup(800, 600)  # Set the size of the turtle window

turtle.penup()
turtle.goto(-200, 50)  # Move the turtle to the center of the screen
turtle.pendown()

turtle.bgcolor("black")
turtle.pencolor("white")

def draw_pentagram(size):
    for i in range(1000):
        hue = i / 100.0
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        turtle.pencolor(rgb)
        turtle.forward(size)
        turtle.right(140)

turtle.speed(100)
pentagram_size = 350
draw_pentagram(pentagram_size)
turtle.done()
