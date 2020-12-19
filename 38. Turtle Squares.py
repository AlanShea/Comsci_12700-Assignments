#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: October 27, 2020

import turtle

def squares(t, length):
    if length > 10:
        for i in range(4):
            t.forward(length)
            t.left(90)
        squares(t, length/2)

def nestedSquares(t, length):
    if length > 10:
        for i in range(4):
            t.forward(length)
            t.left(90)
            nestedSquares(t, length/2)

