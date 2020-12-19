#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: October 20, 2020

import pandas as pd 
import matplotlib.pyplot as plt 

fileIn = input("Enter name of input file:   ")
fileOut = input("Enter name of output file:  ")

data = pd.read_csv(fileIn)
data["Fraction Single Women"] = data["Single Adult Women in Shelter"] / data["Total Individuals in Shelter"]
data.plot(x = "Date of Census", y = "Fraction Single Women")

dataGraph = plt.gcf()
dataGraph.savefig(fileOut)
