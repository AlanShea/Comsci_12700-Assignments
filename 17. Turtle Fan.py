#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: September 22, 2020

import turtle

scr = turtle.Screen()
stampy = turtle.Turtle()
stampNum = int(input ("Enter a number of stamps: "))
stampy.shape("circle")
stampy.penup()
steps = 20
for i in range (stampNum):
    stampy.stamp()
    if i % 4 == 0:
        steps = steps + 2
    stampy.forward(steps)
    stampy.right(24)

scr.exitonclick ()
