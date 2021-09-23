########################################################################
##
## CS 101 Lab
## Program 3
## Name
## Email
##
## PROBLEM : Guess number btwn 1-100 based on remainder of  3,5, and 7.
##
## ALGORITHM : 
##      1.ask them to think of a number btwn 1-100
##      2.ask for remainder of 3
##      3.check to make sure remainder is possible, if no ask for remainder again
##      4.ask for remainder of 5
##      5.check to make sure remainder is possible, if no ask for remainder again
##      6.ask for remainder of 7
##      7.check to make sure remainder is possible, if no ask for remainder again
##      8.check remainders agaisnt all possible remainders for numbers 1-100
##      9.Ask if they want to continue playing
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
print('Welcome to the Flarsheim Guesser!')
play = 'y'
remainders = [0,0,0] # list place holder
while play == 'y':
    count = 0
    print('Please think of a number between 1 and 100') 
    for x in range(3,7+1,2):
        remainders[count] = (int(input('What is the remainder of your number when it is divided by {}?\n'.format(x))))# replaces placeholder with the remainder of division by 3,5,7 as integer
        while (remainders[count]>= x) or (remainders[count] < 0):#ensures that outside of bounds inputs are checked
            if remainders[count] >= x:
                while remainders[count] >= x:
                    print('Remainder must be less than {}'.format(x)) #ensuring remainder stays within possible values
                    remainders[count] = int(input('What is the remainder of your number when it is divided by {}?\n'.format(x)))#remainder of division by 3,5,7 as integer
            elif remainders[count] < 0:
                while remainders[count] < 0:
                    print('Remainder must be 0 or greater') #ensuring remainder stays within possible values
                    remainders[count] = int(input('What is the remainder of your number when it is divided by {}?\n'.format(x)))#remainder of division by 3,5,7 as integer
        count +=1 #used to switch btwn remainders in list
    while remainders[1] == remainders[2]: #ensureing remainders from divison of 5 and 7 are not equal
        print('Remainder of 7 must not be equal to the remainder of 5') #ensuring remainder stays within possible values
        remainders[2] = int(input('What is the remainder of your number when it is divided by 7?\n'))#remainder of division by 3,5,7 as integer
    for r in range(1,101): #checks for the remainders from numbers 1-100 when divided by 3,5,7
        remain1 =  r % 3
        remain2 = r % 5
        remain3 = r % 7
        if remain1 == remainders[0] and remain2 == remainders[1] and remain3 == remainders[2]:
            print('Your number was {}!'.format(r))
            print('How amazing is that!')
    play = input('Do you want to play again? Y to continue, N to quit\n')
    while (play != 'y') and (play !='n') and (play !='Y') and (play !='N'): # Ensureing they enter correctly to exit or continue
        play = input('Do you want to play again? Y to continue, N to quit\n')
    if play == 'Y':# making capital y work aswell
        play = 'y'
    continue
