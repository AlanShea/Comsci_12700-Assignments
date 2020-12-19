import numpy as np
import matplotlib.pyplot as plt
elevations = np.loadtxt('elevationsNYC.txt')
# Base image size on shape (dimensions) of the elevations:
mapShape = elevations.shape + (3,)
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations [row, col] == 0:
            floodMap [row, col, :] = 1.0
        else:
            floodMap [row, col, 0:3:2] = 1.0


plt.imsave('floodMap.png', floodMap)
