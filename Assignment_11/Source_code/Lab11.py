###################################################################
##
## CS 101 Lab
## Program 11
## Name: Nicholas Frede
## Email
##
## PROBLEM : Create a clock
##
## ALGORITHM : 
##      1. Have a class called clock takes hour, minute, second, and clocktype. Have an alternate hour and pm am. This is donce by converting from a 24 hour to a 12. 13-23 is pm while 24 and 0-12 is am.
##      2. The hour is converted to 12 hour by if the clock is 0 its 12, if above 12 its the hour -12. if its anything else its the same as 24 hour.
##      3. Next a string is defined to print depending on weather it is a 12 hour or a 24 hour. hour:minute:second and if 12 it has am or pm
##      4. Next a tick is defined. Using if and else statements it will add one second and if it was below 59 if above it increases the minute by one and resets to zero. Same is done once minutes reach 59 and the seconds is also 59.
##      5. In the main code first is importing time. Then ask user for the currect time hour, minute, second, and clocktype. Using the time to sleep for ne second I continuallt tick and print the time.
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import time
class Clock:
    def __init__(self, hour, minute, second, clocktype = 0):
        '''sets all values equal to corresponding arguments and sets and alternate hour and am or pm based on the hour'''
        self.hour = hour
        self.minute = minute
        self.second = second
        self.clocktype = clocktype
        if self.hour >= 13 and self.hour != 24: # pair of if/else to match am or pm to correct time
            self.half = 'pm'
        else:
            self.half = 'am'
        if self.hour == 0: # if/elif/else statements to convert  time to type 1
            self.hour1 = 12
        elif self.hour >= 13:
            self.hour1 = self.hour - 12
        else:
            self.hour1 = self.hour
    def __str__(self):
        '''returns time depending on the clocktype'''
        if self.clocktype == 0:#checks clock type and returns correct responce
            return '{:02}:{:02}:{:02}'.format(self.hour, self.minute, self.second)
        elif self.clocktype == 1:
            return '{:02}:{:02}:{:02} {}'.format(self.hour1, self.minute, self.second, self.half)
    def tick(self):
        '''Adds a second to the clock and adjusts for it'''
        if self.hour == 24:#resets once 24 hours is reached
            self.hour = 0
            self.minute = 0
            self.second = 0
        if self.second < 59:# # adds a second if its not yet reach 59
            self.second += 1
        else:# rests seconds to 0 and adds 1 to minutes
            self.second = 0
            if self.minute < 59: # adds a minute if its not yet reach 59
                self.minute += 1
            else:# rests minutes to 0 and adds 1 to hours
                self.minute = 0
                self.hour += 1
        if self.hour >= 13 and self.hour != 24:# pair of if/else to match am or pm to correct time after each tick
            self.half = 'pm'
        else:
            self.half = 'am'
        if self.hour == 0:# if/elif/else statements to convert  time to type 1 after each tick
            self.hour1 = 12
        elif self.hour >= 13:
            self.hour1 = self.hour - 12
        else:
            self.hour1 = self.hour

if __name__ == "__main__":
    lst = ['hour','minute','second']
    lst2 =[]# placeholder to put input
    for i in lst:# go through all options to ask
        a = True
        while a == True:#ensures correct and valid input is entered
            try:
                x = int(input('What is the current {}: '.format(i)))
                if i != 'hour':
                    if x not in range(0,60):#makes sure minutes and seconds are in range possible
                        print('please enter a valid {} of the day'.format(i))
                    else:
                        lst2.append(x)#appends to list 
                        a = False
                else:
                    if x not in range(0, 25):#ensures possible hour of the day
                        print('please enter a valid {} of the day'.format(i))
                    else:
                        lst2.append(x)#appends to list
                        a = False
            except ValueError:
                print('please enter a valid {} of the day'.format(i))
    clock1=Clock(lst2[0],lst2[1],lst2[2])
    while True:#while loop to count time
        print(clock1)
        time.sleep(1)
        clock1.tick()
 
