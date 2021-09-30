########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Need a set of functions that will allow the user to gamble with a banked amount of money and see if they get a profit.
##
## ALGORITHM : 
##      1. Import random module
##      2. Create a function that will ask if the user if they want to play again.
##      3. If the enter Yes or a variation of yes  play the code again. If they enter No or a variation of No end the code. If aything outside  yes or no reask the question.
##      4. Create a function that will ask for the amount they would like to wager. Repeating if they answer outside of the bounds of 0 to the bank amount.
##      5. Create a function that will generate 3 random numbers between 1 and 10.
##      6. Create a function that will see how many matches are in 3 different numbers.
##      7. Create a function that will ask the user how many chips they want to start with. Repeat if value outside of bounds 1-100.
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    play = 'a' #placeholder so while loop starts
    while play != 'NO' or play !='N' or play != 'YES' or play !='Y':#repeats if input is outside of expected bounds
        play = input('Do you want to play again:\n')#asks fo their input
        play = play.upper()#Puts the enitre string entered in upper case. So the input caps wont matter.
        if play == 'YES' or play =='Y':#checks the input to see if they want to play again
            return True
        elif play == 'NO' or play =='N':#checks the input if they want to play again
            return False
        else:
            print('You must enter Y/YES/N/NO. Please try again.')
            continue#restarts loop as the input was outside of bounds
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    amount = int(input('Enter the amount you want to wager:\n'))
    while amount <= 0 or amount > bank:
        if amount <= 0:
            print('The wager cant be less than or equal to 0. Please try again.')
        if amount > bank:
            print('The wager cant be greater than the amount in the bank. Please try again.')
        amount = int(input('Enter the amount you want to wager:\n'))
    return amount            

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    a = random.randint(1,10)#gets random number between 1-10
    b = random.randint(1,10)#gets random number between 1-10
    c = random.randint(1,10)#gets random number between 1-10
    return a, b, c

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb and reela == reelc:
        return 3
    if reela == reelb and reela != reelc:
        return 2
    if reela != reelb and reela == reelc:
        return 2
    if reelb == reelc and reela != reelc:
        return 2
    if reela != reelb and reela != reelc:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    amount = 0#placeholder to start loop
    while amount <=0 or amount > 100:
        amount = int(input('How many chips do you want to play with?\n'))#gets entered amount
        if amount <= 0:#checks if amount is within bounds, if not repeats
            print('Amount too low, the number needs to be between 1-100. Try again.')
            continue#resets loop since value is outside of bounds
        elif amount > 100:#checks if amount is within bounds, if not repeats
            print('Amount too high, the number needs to be between 1-100. Try again.')
            continue#resets loop since value is outside of bounds
    return amount

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 0:# profit for 0 matches based on wager
        profit = wager * -1
    elif matches == 2:# profit for 2 matches based on wager
        profit = wager * 3 - wager
    elif matches == 3:# profit for 3 matches based on wager
        profit = wager *10 - wager
    return profit    


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()