#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: October 14, 2020

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv("nycHistPop.csv", skiprows = 5)

bor1 = input("Enter first borough name: ")
bor2 = input("enter second borugh name: ")
sav = input("Enter output file name: ")

pop["Fraction"] = (pop[bor1] / pop["Total"]) + (pop[bor2] / pop["Total"])

pop.plot(x = "Year", y = "Fraction")

fig = plt.gcf()
fig.savefig(sav)