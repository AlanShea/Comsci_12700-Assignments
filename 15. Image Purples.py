#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: September 15, 2020

import matplotlib.pyplot as plt
import numpy as np

name = input('Enter name of the input file: ')
img = plt.imread(name) 

img2 = img.copy() 
img2[:,:,1] = 0

name = input('Enter name of the output file: ')
plt.imsave(name, img2)
