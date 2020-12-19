#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: November 10, 2020

print('----------------------------------------')
print('Welcome to the total with tax calculator')
print('----------------------------------------')
print('Please enter the price of each item you would like to purchase, one at a time.')
print('Enter a negative number when you are done.')

initValues = float(input('Enter the price of an item: '))
finValue = 0
while initValues > 0:
    calcValue = initValues + initValues * .0875
    finValue = finValue + calcValue
    initValues = float(input('Enter the price of an item: '))

print('The total with tax is $', finValue)
