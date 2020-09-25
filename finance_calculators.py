#Program: finance_calculators.py
#Purpose: Program that allows user to access two different financial calculators

import math

P = 0.0
r = 0.0 
t = 0.0
A = 0.0
B = 0.0
i = 0.0
n = 0.0

#Financial calculator to calculate investment or bond

    #This program is used to calculate user's investment if they choose any of the two option
user = str(input('Kindly choose either (investment or bond) to proceed: ')) 
if user.lower() == 'investment':
    print ('Your selection is', str(user))

    P = float(input('Please enter the amount of money you are depositing: '))
    print ('You have entered', 'R', P)
    r = float(input('Please enter your interest rate: '))
    r = r / 100
    t = int(input('Please enter the number of years you plan to invest on: '))
    print ('You have entered', (t),'years')

    interest = str(input('Kindly choose if (compound or simple) interest: '))
    if interest.lower() == 'simple':
        print('Your selection is', (interest))
        A = P * (1 + r * t)
        print ('And you will earn',A, 'on your investment.')
    elif interest.lower() == 'compound':
        print('Your selection is', (interest))
        B = P * math.pow ((1+r),t)
        print ('And you will earn',B, 'on your investment.')
    #Calculates total amount that must be paid if user selects bond
elif user.lower() == 'bond':
    print ('Your selecton is', str(user))

    P = float(input('Please enter the present value of your house: '))
    print ('The value of your house is', 'R', P)
    i = float(input('Please enter your interest rate: '))
    i = i / 12
    print ('Your calculated interest rate is', i)
    n = int(input('For how lond would you like to take to repay the bond: '))
    print ('You have choosen to repay in', n, 'months.')
    x = (i * P) / (1 - ( math.pow((1+i), - n )))
    print ('You will pay', 'R',x, 'on your home loan.')
    #If no selection, program will ask user to choose
else:
    print ('Wrong selection, please choose between', 'investment or bond:')
