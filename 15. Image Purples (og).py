#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: September 15, 2020

import matplotlib.pyplot as plt
import numpy as np

name = input('Enter name of the input file: ')
img = plt.imread(name)   #Read in image from csBridge.png
plt.imshow(img)		                 #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy()        #make a copy of our image
img2[:,:,1] = 0          #Set the green channel to 0

plt.imshow(img2)         #Load our new image into pyplot
plt.show()               #Show the image (waits until closed to continue)

name = input('Enter name of the output file: ')
plt.imsave(name, img2)  #Save the image we created to the file: reds.png
