#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: September 22, 2020

cents = int (input ("Enter a number of cents: "))
print ("Quarters: " + str (cents // 25))
rem = cents % 25
print ("Dimes: " + str (rem // 10))
rem = rem % 10
print ("Nickels: " + str (rem // 5))
print ("Cents: " + str (rem % 5))
