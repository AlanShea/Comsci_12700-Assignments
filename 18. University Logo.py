#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: September 22, 2020

import matplotlib.pyplot as plt
import numpy as np

img = np.ones((30, 30, 3))
img [ : , :10, 0:2] = 0
img [ : , 20: , 0:2] = 0
img [20: , : , 0:2] = 0

plt.imsave ("logo.png", img)


