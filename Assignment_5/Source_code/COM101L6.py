
########################################################################
##
## CS 101 Lab
## Program 5
## Name
## Email
##
## PROBLEM : Check digits in New Linda Hall Librabry card to see if valid and the matching information
##
## ALGORITHM : 
##      1.Import string
##      2.Define function character_value. Use import string module to return Characters as number following 'A'=0,'B'=1 pattern.
##      3.Define a function called get_check_digits. The function will calculate the check digit. This is done by taking the sum of values times the index.
##      4.Define a function called verify_check_digit. If length of string is not 10 return false. If the first five characters are not letters return false. 
##      5.In verify_check_digit if the last three are not numbers return false. If the 6th character is not 1,2, or 3 return false. If the 7th character is not 1,2,3, or 4 return fasle. 
##      6.In function of verify_check_digit, if the calculated check digit does not match the inputed check digit return false. Otherwise return true
##      5.Define a function get_school. If 1 then School of Computing and Engineering SCE. If 2 then School of Law. If 3 then College of Arts and Sciences.
##      6.Define a ducntion get_grade. If the input is 1,2,3, and 4  then Freshmen, sohpmore, Junior, and Senior in the corresponding order.
##      7.Display a title
##      8.A repeating loop is outside of the main code. press enter to exit loop and end program
##      9.When verify_check_digi is True display the school and grade. If false display error
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import string


def character_value(char : str) -> int:
    ''' Returns 0 for A, 1 for B, etc. '''
    return string.ascii_uppercase.index(char) 
def get_check_digit(idnumber : str) -> int:
    ''' Returns the check digit for the name and sid. '''
    total = 0
    for i in range(0,5):
        total += ((i + 1) * character_value(idnumber[i])) #gets the values and indexs and times them togther, the adds them to the total
    for i in range(5,10):
        total += ((i + 1) *int(idnumber[i]))
    return total % 10 #returns the check digit
def verify_check_digit(idnumber : str) -> tuple:
    ''' returns 2 values bool and a string with errors if bool is False and else returns True '''
    if len(idnumber) != 10:
        return False, 'The length of the number given must be 10' #if the length of the entered string is not 10 returns false
    elif idnumber[0:5].isalpha() != True: #checks to see if entered string from 0-4 are letters
        for i in range(0,5):
            if idnumber[i].isalpha() !=True: #checks to see where the error occured in the string
                return False, 'The first 5 characters must be A-Z, the invalid character is at {} is {}'.format(idnumber[i], i)
    elif idnumber[7:10].isdigit() != True: #checks to see if entered string from 0-4 are letters
        for i in range(7,10):
            if idnumber[i].isdigit() !=True: #checks to see where the error occured in the string
                return False, 'The last three characters must be 0-9, the invalid character is at {} is {}'.format(idnumber[i], i)
    elif idnumber[5] != '1' and idnumber[5] != '2' and idnumber[5] != '3': # checks that index 5 is either 1,2, or 3
        return False, 'The sixth character must be 1 2 or 3'
    elif idnumber[6] != '1' and idnumber[6] != '2' and idnumber[6] != '3' and idnumber[6] != '4': # checks that index 6 is 1 to 4
        return False, 'The seventh character must be 1 2 3 or 4'
    elif int(idnumber[9]) != get_check_digit(idnumber): #checks if the entered last digit matches the calculated last digit
        return False, 'Check Digit {} does not match calculated value {}'.format(idnumber[9], get_check_digit(idnumber))
    else:
        return True, ''
def get_school(idnumber : str) -> str: #Returns appropriate school for index
    ''' Returns the school the 5th index or 6th character is for. '''
    if idnumber[5] == '1':
        return 'School of Computing and Engineering SCE'
    elif idnumber[5] == '2':
        return 'School of Law'
    elif idnumber[5] == '3':
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'
def get_grade(idnumber : str) -> str: #Returns appropriate  grade for index
   '''Returns the grade for index 6'''
   if idnumber[6] == '1':
       return 'Freshman'
   elif idnumber[6] == '2':
       return 'Sophomore'
   elif idnumber[6] == '3':
       return 'Junior'
   elif idnumber[6] == '4':
       return 'Senior'
   elif idnumber[6] == '5':
       return 'Invalid Grade'

if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:

        print()
        card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()
        if card_num == "":
            break
        result, error = verify_check_digit(card_num)
       
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            print("Libary card is invalid.")
            print(error)
        
