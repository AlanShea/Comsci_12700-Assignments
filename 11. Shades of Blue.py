#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: September 15, 2020

import turtle

scr = turtle.Screen()

scr.colormode (255)
tess = turtle.Turtle ()
tess.shape ('turtle')
tess.backward (100)

for i in range (0, 255, 10):
    tess.forward (10)
    tess.pensize (i)
    tess.color (0, 0, i)

for i in range (255, 0, -10):
    tess.forward (10)
    tess.pensize (i)
    tess.color (0, 0, i)

scr.exitonclick ()
