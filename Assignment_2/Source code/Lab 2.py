########################################################################
##
## CS 101 Lab
## Program 2
## Name Nicholas Frede
## Email njfccq@umkc.edu
##
## PROBLEM : Need to calculate grades.
##
## ALGORITHM : 1-ask for the name of student
##             2-ask for grade of lab
##             3-lab value should've been 0-100
##             4-if the lab value is above 100 change to 100, if lab value is below 0 change to 0
##             5-ask for grade of exam
##             6-exam value should've been 0-100
##             7-if the exam value is above 100 change to 100, if exam value is below 0 change to 0
##             8-ask for grade of attendance
##             9-attendance value should've been 0-100
##             10-if the attendance value is above 100 change to 100, if attendance value is below 0 change to 0
##             11-calculate total grade based on weight and value of each entered grade
##             12-assign A if total grade above or equal to 90
##             13-assign B if total grade 80-89
##             14-assign C if total grade 70-79
##             15-assign D if total grade 60-69
##             16-assign F if total grade below 60
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      The  first if/elif statements are used to differentiate proper input and erroneous input.
##      The second if/elif/elif/elif/elif/else is to assign letter grade based on  total_grade.
##
########################################################################
print('***Welcome to Grade Calculator***')
name = input('Enter name of student:\n')
print()
lab = int(input('Enter lab grade?\n'))
if lab > 100:
    print('The lab value entered should\'ve been 100 or less. It has been changed to 100')
    lab = 100
elif lab < 0:
    print('The lab value entered should\'ve been 0 or greater. It has been changed to 0')
    lab = 0
print()
exam = int(input('Enter exam grade?\n'))
if exam > 100:
    print('The exam value entered should\'ve been 100 or less. It has been changed to 100')
    exam = 100
elif exam < 0:
    print('The exam value entered should\'ve been 0 or greater. It has been changed to 0')
    exam = 0
print()
attendance = int(input('Enter attendance grade?\n'))
if attendance > 100:
    print('The attendance value entered should\'ve been 100 or less. It has been changed to 100')
    attendance = 100
elif attendance < 0:
    print('The attendance value entered should\'ve been 0 or greater. It has been changed to 0')
    attendance = 0
total_grade = lab * 0.7 + exam * 0.2 + attendance * 0.1 #calculate total grade based on weight
if total_grade >= 90:
    letter_grade = 'A'
elif total_grade >= 80:
    letter_grade = 'B'
elif total_grade >= 70:
    letter_grade = 'C'
elif total_grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'
print()
print('The weighted grade for',name,'is',total_grade)
print(name,'has a letter grade of',letter_grade)
print('***Thank you for using Grade Calculator***')

