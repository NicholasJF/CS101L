###################################################################
##
## CS 101 Lab
## Program 8
## Name: Nicholas Frede
## Email
##
## PROBLEM : Find vehicles in a file that have above a certain mpg. Output those vehicles.
##
## ALGORITHM : 
##      1. Create Menu function. Displays all options. If 1 run function tadd(). If 2 run trem(). If 3 or 6 clear lst. If 4 run aadd(). If 5 run arem(). If D run display(). If q break.
##      2. Create a function that appendes the list entered with the entered value. If outside of bounds reasks for value. This is tadd() and aadd() function. The difference is display test vs assignment.
##      3. Create a function that removes the entered value from the list. If outside of bounds do not remove value. This is trem)( and arem(). The dfference is display test vs assignment.
##      4. Create a function that takes That displays the number of entered values, max, min, avg, and std. This is done for both test and assignemnts. If nothing entered returns n/a. Weighted grade is 0.00 if nothing entered.
##      5. Create a function that takes a list and returns the standard deviation of the list.
##      6. For the main code run fune menu function and have two empty list as arguments in the menu function.
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

def menu(tlst, alst):
    '''Displays all options and runs through their functions'''
    while True:
        print('{:^40}'.format('Grade Menu')) #formats and displays title
        print('1 -Add Test')
        print('2 -Remove Test')
        print('3 -Clear Tests')
        print('4 -Add Assignment')
        print('5 -Remove Assignment')
        print('6 -Clear Assignments')
        print('D -Display Scores')
        print('Q -Quit')
        choice = input('Enter choice:\n')#input to decide what below shall be ran
        if choice == '1':
            tadd(tlst)
        elif choice == '2':
            trem(tlst)
        elif choice == '3':
            tlst.clear()
        elif choice == '4':
            aadd(alst)
        elif choice == '5':
            arem(alst)
        elif choice == '6':
            alst.clear()
        elif choice == 'D' or choice == 'd':
            display(tlst, alst)
        elif choice == 'Q' or choice == 'q':
            break
        else:
            print('Enter a valid choice.')
        print()#gives empty line for formatting
def tadd(lst):
    '''adds a score to the test list'''
    while True: #while loop to keep going until a valid value is entered
        try:#In case entered causes error 
            num = float(input('Enter score between 1-100\n'))
            if num >= 0:# value must be greater than -1
                lst.append(num)
                break
            else:
                print('Entered number must be greater than -1')
                print()
        except ValueError:
            print('Entered value must be a number')
            print()
def trem(lst):
    '''removes a score from the test list'''
    try:#checks that entered value is valid
        rem = float(input('Enter score of test you want removed\n'))
        try:#checks that entered value is valid
            lst.remove(rem)
        except ValueError:
            print('Test Score could not be found')
            print()
    except ValueError:
        print('Entered value must be a number')
        print()
def aadd(lst):
    '''adds a score to the assignment list'''
    while True:
        try:
            num = float(input('Enter score between 1-100\n'))
            if num >= 0:
                lst.append(num)
                break
            else:
                print('Entered number must be greater than -1')
                print()
        except ValueError:
            print('Entered value must be a number')
            print()
def arem(lst):
    '''removes a score from the assignment list'''
    try:#checks that entered value is valid
        rem = float(input('Enter score of assignment you want removed\n'))
        try:#checks that entered value is valid
            lst.remove(rem)
        except ValueError:
            print('Assignment Score could not be found')
            print()
    except ValueError:
        print('Entered value must be a number')
        print()
def display(tlst, alst):
    '''Displays the results of the lists'''
    if True:
        print('{:<20}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('Type', '#','min','max','avg', 'std'))
        print('{:=<70}'.format('='))
        try:#displays if list not empty
            print('{:<20}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('Test', len(tlst),min(tlst),max(tlst),sum(tlst)/len(tlst), std(tlst)))
        except ValueError:#displays if list empty
            print('{:<20}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('Tests', 0,'n/a','n/a','n/a', 'n/a'))
        try:#displays if list not empty
            print('{:<20}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('Programs', len(alst),min(alst),max(alst),sum(alst)/len(alst), std(alst)))
        except ValueError:#displays if list empty
            print('{:<20}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('Programs', 0,'n/a','n/a','n/a', 'n/a'))
        print()
        try:
            print('{:<20}{:<5}'.format('The weighted scores is', (sum(tlst)/len(tlst))*0.6 + (sum(alst)/len(alst))*0.4 ))
        except ZeroDivisionError:
            print('{:<20}{:<5.2f}'.format('The weighted scores is ', 0))
def std(lst):
    '''Gets std from a list'''
    mean = sum(lst)/len(lst)
    total = 0
    for i in range(len(lst)):
        total += (lst[i]-mean)**2
    tot = (total/len(lst))**0.5
    return tot
test = []
assignment = []
menu(test, assignment)
