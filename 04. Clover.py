#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: September 1, 2020

import turtle

win = turtle.Screen()

clover = turtle.Turtle()
clover.shape("turtle")
clover.color("purple")

for i in range(15):
    clover.forward(50)
    clover.left(24)

clover.left(125)

for i in range(15):
    clover.forward(50)
    clover.left(24)

clover.left(125)

for i in range(15):
    clover.forward(50)
    clover.left(24)

win.exitonclick()
