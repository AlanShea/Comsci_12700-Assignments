#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: October 6, 2020

import numpy as np
import matplotlib.pyplot as plt

img = plt.imread(input("Enter file name:   "))

snow = 0
t = 0.8

for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        if ((img[row, col, 0] > t) and (img[row, col, 1] > t) and (img[row, col, 2] > t)):
            snow = snow + 1

print("Snow count is", snow)