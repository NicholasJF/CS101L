###################################################################
##
## CS 101 Lab
## Program 7
## Name: Nicholas Frede
## Email
##
## PROBLEM : Find vehicles in a file that have above a certain mpg. Output those vehicles.
##
## ALGORITHM : 
##      1. Create min_mpg function. This gets the min mpg from the user. If below 1 repeat, If above 100 repeat, if value error repeat. If the user num passes all the mpg is returned.
##      2. Create a function that asks user to enter vehicle file. If user enters an invalid file tell them then repeate.
##      3. Create a function asks the user for what file they want to output. Have the file be write a. If IOERROR repeate function. Return open file.
##      4. Create a function that takes the file from step 2 and read each line of the file as a list. Make line a nested list. Return nested list.
##      5. Create function that outputs the file. The function takes in the list from step 4, the mpg from step 1, and the outfile from step 3. Check if each combined mpg of each nested list is below the mpg entered. If not write to file.  If invalid entered print an statment telling what was not entered.
##      6. For the main code run function 1, function 2, function 4, function 3, function 5. Clost both files.
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

def min_mpg():
    '''Gets Minimum Fuel Economy from user anc checks for errors and its bounds'''
    a = True
    while a == True: #loop to run entire program as long as mpg is not returned
        try:
            while a == True: #loop to run as long as no error but value is out of bounds
                mpg = float(input('Enter the minimum mpg: '))
                if mpg <= 0:
                    print('Fuel economy given must be greater than 0\n')#tell how they are out of bounds
                elif mpg > 100:
                    print('Fuel economy must be less than 100\n')#tell how they are out of bounds
                else:
                    a = False #ends loop
                    return mpg #gives mpg
        except ValueError:
            print('You must enter a number for the fuel economy')
def get_file():
    '''Opens the file the user enters. Will continue to ask until a file with a valid name is entered'''
    a = True #placehold to start loop
    while a == True:#loop to run code as long as error occurs
        try:
            file = input('Enter the name of the input vehicle file: ')
            myfile = open(file)
            a = False #ends loop after iteration
            return myfile#gives the open file
        except FileNotFoundError:
            print('Could not open file {}'.format(file))
def get_outputfile():
    '''Creates the Output file and will repeate until a valid name is entered.'''
    a = True #placehold to start loop
    while a == True:#loop to run code as long as error occurs
        try:
            file = input('Enter the name of the file to output to: ')
            myfile = open(file, 'a')
            a = False #ends loop after iteration
            return myfile#gives the open file
        except IOError:
            print('There is an IO Error {}'.format(file))
def file_split_list(myfile):
    '''Creates a nested list of the lines of the file entered, with /t as the seperator'''
    file1 = myfile.readlines()
    file2 = []
    for i in range(len(file1)):
        file2.append(file1[i].split('\t'))
    return file2
def file_output(lst, mpg, outfile):
    '''Writes the vehicles above the entered mpg to the outfile. The vehicles come from lst.'''
    for i in range(1, len(lst)):
        try:
            combinded = float(lst[i][7])
            if combinded >= mpg:
                outfile.write('{:<5}{:<20}{:<40}{:>10.3f}\n'.format(lst[i][0], lst[i][1], lst[i][2], combinded))
        except ValueError:
            print('Could not convert value {} for vehicle {} {} {}'.format(lst[i][7], lst[i][0], lst[i][1], lst[i][2]))
if __name__ == "__main__":
    mpg = min_mpg()
    infile = get_file()
    lst = file_split_list(infile)
    outfile = get_outputfile()
    file_output(lst, mpg, outfile)
    infile.close()
    outfile.close()
            
