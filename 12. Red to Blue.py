#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: September 15, 2020

import turtle

scr = turtle.Screen()

scr.colormode (255)
tess = turtle.Turtle ()
tess.shape ('turtle')
tess.backward (200)

for i in range (0, 255, 10):
    tess.forward (20)
    tess.pensize (i)
    tess.color (255 - i, 0, i) 

scr.exitonclick ()
