#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: September 15, 2020

import turtle

scr = turtle.Screen ()

shelly = turtle.Turtle ()
shelly.shape ('turtle')

color = input ("Please enter a 6-digit Hexadecimal number: ")
shelly.color("#" + color)
shelly.stamp ()

scr.exitonclick ()
