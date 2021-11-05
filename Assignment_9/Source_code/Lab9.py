###################################################################
##
## CS 101 Lab
## Program 9
## Name: Nicholas Frede
## Email
##
## PROBLEM : Find vehicles in a file that have above a certain mpg. Output those vehicles.
##
## ALGORITHM : 
##      1. Import csv module. Create month_from_number function. Match number entered to appopriate value in list and return value.
##      2. Create read_in_file function that opens and reads the file and returns as a list.
##      3. Create create_reported_date_dict function. Creates a dict. Runs through entire list and if date exists in the dictioary add one to the number if not add the date and set the value to 1. 
##      4. Create create_reported_month_dict function. Isolates the month from rest of date. Creates a dict. Runs through entire list and when it encounters the month if the month exists in the dictioary add one to the number if not add the date and set the value to 1. 
##      5. Create create_offense_dict function. Creates a dict. Runs through entire list and if offense exists in the dictioary add one to the number if not add the date and set the value to 1. 
##      6. Create create_offense_by_zip function. Creates a dict. Run through entire list. If Offense is not in dict add to dict and add the zip and 1. If the offense is already in the dict and zip is not add zip with value as 1 as a nested dict. If the offense is already in the dict and zip is add 1 to the nested dict. 
##      7. For the main code run ask for the file name. Enter file into read_in_file function. If invalid reask. Use create_reported_month_dict with list. Use month_from_number to convert month num to a name. Display maximum number of offenses commited on one month.
##      8. Use create_offense_dict function with the list from read_in_file. Display maximum number of offenses commited on one type of offense.
##      9. Ask user for an offense. Use create_offense_by_zip function with the list from read_in_file. Check if offense is in the returned dict. If not reask. Loop through the nested dict in the offense. Display each one and their respective value.
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import csv
def month_from_number(num):
    '''converts numerical month to word'''
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']#list of months
    return months[num-1]#returns month based on list
def read_in_file(file):
    '''Takes csv file and turns into nested list'''
    file1 = open(file, encoding= 'utf-8')
    csvlist = list(csv.reader(file1, delimiter=','))
    return csvlist
def create_reported_date_dict(lst):
    '''creates a dict with date as key and number if crimes as value'''
    date_count = {}
    for i in range(1, len(lst)): #run through all lines except title line
        if lst[i][1] in date_count:#checks if already in dict
            date_count[lst[i][1]] += 1#adds one if in dict
        else:
            date_count[lst[i][1]] = 1#adds key and sets value equal to 1 
    return date_count
def create_reported_month_dict(lst):
    '''creates a dict with month as key and number if crimes as value'''
    month_count = {}#empty dict to be filled
    for i in range(1, len(lst)):
        a = lst[i][1].split('/')#splits each date to isolate the month num
        a = list(map(int, a))#turns all month num from string to int
        if a[0] in month_count:#adds  +=1 to month if the month is in dict
            month_count[a[0]] += 1
        else:#adds the month num =1 if the month is not in dict
            month_count[a[0]] = 1
    return month_count
def create_offense_dict(lst):
    '''creates a dict with offense as key and number if crimes as value'''
    offense_count = {}
    for i in range(1, len(lst)): #run through all lines except title line
        if lst[i][7] in offense_count:#checks if already in dict
            offense_count[lst[i][7]] += 1#adds one if in dict
        else:
            offense_count[lst[i][7]] = 1#adds key and sets value equal to 1 
    return offense_count
def create_offense_by_zip(lst):
    '''Create nested Dict with offense as key in outside dict, zip as key inner dict with num of crimes as value'''
    offense_zip = {}
    for i in range(1, len(lst)):
        if lst[i][7] not in offense_zip.keys():
            offense_zip[lst[i][7]] = {lst[i][13]: 1}
        elif lst[i][13] not in offense_zip[lst[i][7]]:
            offense_zip[lst[i][7]][lst[i][13]] = 1
        elif lst[i][13] in offense_zip[lst[i][7]]:
            offense_zip[lst[i][7]][lst[i][13]] += 1
        else:
            continue
    return offense_zip
if __name__ == "__main__":
    a = True # placeholder to start loop
    while a == True:# while loop to rerun if file not found
        try:#run if file is valid
            file = input('Enter in the name of the crime data file: ')
            lst = read_in_file(file)
            a = False
        except FileNotFoundError:#run if file is invalid
            print('Could not find file {}.'.format(file))
    print()#space to help display
    month_num = create_reported_month_dict(lst)
    max_crime = max(month_num.values())
    for key in month_num:#checks for max number of values and finds the key
        if month_num[key] == max_crime:
            month = key
    name_month = month_from_number(month)
    print('The month with the highest # of crimes is {} with {} offenses.'.format(name_month , max_crime))
    offense_num = create_offense_dict(lst)
    max_crimeo = max(offense_num.values())
    for key1 in offense_num:#checks for max number of values and finds the key
        if offense_num[key1] == max_crimeo:
            offense = key1
    name_offense = offense
    print('The offense with the highest # of crimes is {} with {} offenses.'.format(name_offense , max_crimeo))
    print()#space to help display
    offense_zip = create_offense_by_zip(lst)
    b = True
    while b == True:#while loop to ensure offense is valid
        crime = input('Enter offense: ')
        if crime in offense_zip.keys():
            b = False
        else:
            print('Not a valid offense. Try again.')
    print()#spacer
    print('{} offenses by Zip Code'.format(crime))
    print('{}{:>20}'.format('Zip Code', '# Offenses'))
    print('{:=>30}'.format('='))
    for key2 in offense_zip[crime].keys():#runs through all zips and amounts in that crime
        print('{} {:>20}'.format(key2, offense_zip[crime][key2]))
