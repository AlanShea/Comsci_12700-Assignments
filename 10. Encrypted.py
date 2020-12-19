#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: September 8, 2020

word = input ("Enter a word: ")
coded = ""

for c in word:
    shift = ord(c) - ord("A") + 13
    back = shift % 26
    codeChar = chr(ord("A") + back)
    coded = coded + codeChar

print ("Your word in code is: " + coded)
