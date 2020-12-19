#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: November 10, 2020

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)
wn = turtle.Screen()

for i in range(200):
  a = random.randrange(0,361,30)
  trey.right(a)
  trey.forward(5)

wn.exitonclick()