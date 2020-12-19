#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: September 8, 2020

myString = input ("Enter a string : ")

print (myString)

for c in myString:
    print (c, ord(c)  + 1, chr(ord(c) + 1))
