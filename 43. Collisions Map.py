#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: November 3, 2020

import pandas as pd 
import folium

fileIn = input('Enter CSV file name:    ')
fileOut = input('Enter output file:     ')

colData = pd.read_csv(fileIn)

collisionMap = folium.Map(location = [0, 0], zoom_start = 5, tiles = 'Cartodb Positron')
for indes, row in colData.iterrows():
    lat = float(row["LATITUDE"])
    lon = float(row["LONGITUDE"])
    time = row["TIME"]
    folium.Marker(location = [lat, lon], popup = time).add_to(collisionMap)

collisionMap.save(outfile = fileOut)