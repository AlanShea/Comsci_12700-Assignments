#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: September 15, 2020

rawList = input ("Please enter your list of names: ")
splitList = rawList.split("; ")

for i in splitList:
    div = i.find(",")
    print (i [div + 2] + ".", i [:div])
    
print ("\nThank you for using my name organizer")
