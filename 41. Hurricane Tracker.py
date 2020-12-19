#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: November 3, 2020

import turtle
import pandas as pd

def setup(windowTitle):
    screen = turtle.Screen()
    screen.title(windowTitle)

    screen.setup(800, 404)
    screen.setworldcoordinates(-180,-90,180,90)
    screen.bgpic("mapNASA.gif")

    t = turtle.Turtle()
    t.pensize(1)
    t.color('red')
    t.penup()

    return t,screen

def animate(t,lat,lon,wind):
    t.goto(lon, lat)
    t.pendown()

    if wind >= 157:
        t.pensize(5)
        t.color('red')
    elif wind >= 130:
        t.pensize(4)
        t.color('orange')
    elif wind >= 111:
        t.pensize(3)
        t.color('yellow')
    elif wind >= 96:
        t.pensize(2)
        t.color('green')
    elif wind >= 74:
        t.pensize(1)
        t.color('blue')
    else:
        t.pensize(1)
        t.color('white')
    
    return(t)

def main():
    hFile = input('Enter file name: ')
    t, wn = setup(hFile)

    df = pd.read_csv(hFile)
    for index, row in df.iterrows():
        lat = int(row["Lat"])
        lon = int(row["Lon"])
        wind = row["Wind"]
        print(lat,lon,wind)
        animate(t,lat,lon,wind)
    
    wn.exitonclick()

if __name__ == "__main__":
    main()
