#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: November 10, 2020

def monthString(monthNum):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return months[monthNum - 1]

def main():
    monthNum = int(input('Enter the number of the month: '))
    while monthNum <= 0 or monthNum >= 13:
        monthNum = int(input('That is not a valid month number. Please enter a number between 1 and 12: '))
    
    monthStr = monthString(monthNum)
    print('The month is', monthStr)

if __name__ == "__main__":
    main()