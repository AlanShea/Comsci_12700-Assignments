#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: October 13, 2020

import pandas as pd 

fileName = input("Enter file name:  ")
colAvg = input("Enter the name of the column\n(Temperature, Luminosity, Radius, or Absolute Magnitude\nyou would like to average:   ")

data = pd.read_csv(fileName)
groups = data.groupby("Star type").mean()

print("The average", colAvg, "for each Star type is:")
print(groups[colAvg])
