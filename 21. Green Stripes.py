#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: October 6, 2020

import numpy as np
import matplotlib.pyplot as plt

size = int(input("Enter the size:    "))
save = input("Enter output file:    ")

scr = np.ones((size, size, 3))
scr[0:size:2, : , 0:3:2] = 0

plt.imsave(save, scr)
