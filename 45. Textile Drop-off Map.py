#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: November 3, 2020

import pandas as pd 
import folium

fileIn = input('Please enter the name of the input file:    ')
fileOut = input('Please enter the name of the output file:   ')
borough = input('Please enter the name of a borough:    ')

dropMap = folium.Map(location = [40.7, -74.0], zoom_start = 12, tiles = 'Stamen Watercolor')

dropData = pd.read_csv(fileIn)
dropBorough = dropData.groupby("Borough").get_group(borough)

for index, row in dropBorough.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    add = row["Address"]
    folium.Marker(location = [lat, lon], popup = add).add_to(dropMap)

dropMap.save(outfile = fileOut)