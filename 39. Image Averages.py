#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: October 27, 2020

import matplotlib.pyplot as plt 
import numpy as np 

def average(region):
     red = np.average(region[:, :, 0])
     green = np.average(region[:, :, 1])
     blue = np.average(region[:, :, 2])

     return(red,green,blue)

def setRegion(region, r,g,b):     
     region[:, :, 0] = r
     region[:, :, 1] = g
     region[:, :, 2] = b

def quarter(img2, levels):
     h = img2.shape[0]
     w = img2.shape[1]

     hReg = h//2**levels
     wReg = w//2**levels

     for i in range(2**levels):
          for j in range(2**levels):              
               r,g,b = average(img2[i*hReg:(i+1)*hReg,j*wReg:(j+1)*wReg])
               setRegion(img2[i*hReg:(i+1)*hReg,j*wReg:(j+1)*wReg],r,g,b)

def main():
     inFile = input('Enter image file name: ')
     img = plt.imread(inFile)

     for i in range(8):
          img2 = img.copy()
          quarter(img2,i)
     
          plt.imshow(img2)
          plt.show()

     plt.imshow(img)
     plt.show()

if __name__ == "__main__":
     main()