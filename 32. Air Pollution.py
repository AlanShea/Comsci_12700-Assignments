#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: October 21, 2020

import pandas as pd 
import matplotlib.pyplot as plt 

fileIn = input("Enter name of input file:   ")
fileOut = input("Enter name of output file:  ")

data = pd.read_csv(fileIn)

avgAsthma = data.groupby("geo_entity_name").mean()["data_valuemessage"]
avgAsthma.plot.bar()

plt.gcf().subplots_adjust(bottom = 0.5)
dataGraph = plt.gcf()
dataGraph.savefig(fileOut)
