#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: September 1, 2020
#This program draws a star

import turtle
wn = turtle.Screen()

star = turtle.Turtle()
for i in range(5):
    star.forward(100)
    star.left(144)

wn.exitonclick()
