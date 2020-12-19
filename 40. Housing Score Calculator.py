#Name: Alan Q. Shea
#Email: alan.shea65@myhunter.cuny.edu
#Date: October 27, 2020

def computeScore(answers):
    score = 0
    score = score + answers[0]
    if answers[1] >= 23:
        score = score + 1
    if answers[2] == 'Yes':
        score = score - 1
    if answers[3] == 1:
        score = score + 1
    if answers[4] >= 3.5:
        score = score + 1
    return score


def main():
    print('------------------------')
    print('HOUSING SCORE CALCULATOR')
    print('------------------------\n')

    year = int(input('QUESTION 1\nWhat year are you in? (1, 2, 3, 4):  '))
    age = int(input('QUESTION 2\nHow old are you?:  '))
    prob = input('QUESTION 3\nAre you currently on probation? (Yes or No):  ')
    PF = int(input('Are you Part-time or Full-time? (0 or 1):   '))
    gpa = float(input('What is your GPA?:   '))

    answers = [year, age, prob, PF, gpa]

    print('\n-----------------------------')
    print('Your housing score is:   ', computeScore(answers))
    print('-----------------------------')

if __name__ == "__main__":
    main()