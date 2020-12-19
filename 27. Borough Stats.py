#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: October 13, 2020

import pandas as pd 

pop = pd.read_csv("nycHistPop.csv", skiprows = 5)

bor = input("Enter borough: ")
print("Min:     ", pop[bor].min())
print("Max:     ", pop[bor].max())
print("Mean:    ", pop[bor].mean())
print("Median:  ", pop[bor].median())
print("Standard Deviation: ", pop[bor].std())
