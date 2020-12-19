#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: October 27, 2020

import pandas as pd 

fileIn = input('Enter file name:    ')
permits = pd.read_csv(fileIn)

print('There were', len(permits), 'film permits.')
print(permits['Borough'].value_counts())

print('\n\nThe three most popular type of events were:')
print(permits['EventType'].value_counts())