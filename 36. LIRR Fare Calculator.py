#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: October 27, 2020

def computeFare(zone, type):
    if zone == 1:
        if type == 'peak':
            return 8.75
        elif type == 'off-peak':
            return 6.25
    elif zone <= 3:
        if type == 'peak':
            return 10.25
        elif type == 'off-peak':
            return 7.50
    elif zone == 4:
        if type == 'peak':
            return 12.00
        elif type == 'off-peak':
            return 8.75
    elif zone <= 7:
        if type == 'peak':
            return 13.50
        elif type == 'off-peak':
            return 9.75
    else:
        return -1

def main():
    z = int(input('Enter the number of zones:   '))
    t = input('Enter the tcket type (peak/off-peak):    ')
    print('The fare is', computeFare(z, t))

if __name__ == "__main__":
    main()