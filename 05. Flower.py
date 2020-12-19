#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: September 1, 2020

import turtle

scr = turtle.Screen()
scr.bgcolor("hotpink")

trt = turtle.Turtle()
trt.shape("turtle")
trt.pencolor("red")
trt.fillcolor("yellow")

for i in range(36):
    trt.forward(200)
    trt.left(170)
    trt.stamp()

scr.exitonclick()
