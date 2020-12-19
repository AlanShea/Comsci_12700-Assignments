#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: September 22, 2020

sec = int (input ("Please enter the itme in seconds: "))
h = int (sec / 3600)
m = int (sec % 3600 / 60)
s = int (sec % 60)

print (str(h) + "h:", str(m) + "m:", str(s) + "s:")
