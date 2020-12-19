#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: October 21, 2020

import pandas as pd 
import matplotlib.pyplot as plt 

fileIn = input("Enter name of input file:   ")
fileOut = input("Enter name of output file:  ")

data = pd.read_csv(fileIn)

data["Date"] = pd.to_datetime(data["Date"].apply(str))
data["% Attending"] = 100 * (data["Present"] / data["Enrolled"])

data.plot(x = "Date", y = "% Attending")
dataGraph = plt.gcf()
dataGraph.savefig(fileOut)