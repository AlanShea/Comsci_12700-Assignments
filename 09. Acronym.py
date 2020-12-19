#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: September 8, 2020

ph = input ("Enter a phrase: ")
ph = ph.upper()
print ("Your phrase in capital letters: " + ph)

sp = ph.split(" ")
ac = ""

for i in sp:
    ac = ac + i[0]

print (ac)


