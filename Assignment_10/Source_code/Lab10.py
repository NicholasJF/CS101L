###################################################################
##
## CS 101 Lab
## Program 10
## Name: Nicholas Frede
## Email
##
## PROBLEM :Complie and output top ten words, number of unique words, and single words.
##
## ALGORITHM : 
##      1. Define function get_file(). Get file ask for a file from the user. If the file has no error it reads the file and returns the lines. If it has an error then re ask for file.
##      2. Define function word_list(lst). The function takes the list from the file above. splits the list the into 3 lists nested toghter. The non alphabetical words are removed.
##      3. Define function count_dict(lst). Add words from the list that are 3 and greater to a new list. Creates a dict. Runs through entire list and when it encounters the word if the word exists in the dictioary add one to the number if not add the word and set the value to 1.Dict is sorted by values.
##      4. Define words_once(dicts) function. This will go through and count all words that have a value of one
##      5. For the main code t will call the get_file() and put the result into Define function word_list(lst), which will be run through Define function count_dict(lst). The dict from the previous function wil have the top ten displayed and the lenath displayed as unique words. Then the Count_once will run and be displayed as well.
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


def get_file():
    '''Gets file and returns a list of the file, per line'''
    b = True #placeholder to initate loop
    while  b == True:#loop ends only if no error is found
        try:
            file = input('Enter file: ')#gets file
            file1 = open(file)
            a = file1.readlines()
            file1.close()#Closes file once read and turned to list format
            b = False
            return a
        except FileNotFoundError:#Check s for error if error displays print
            print('File could not be found. Please try again.')
def word_list(lst):
    ''' Takes the lst and makes a nested list of each word and a nested list of each letter of the word, removes non letters'''
    for i in range(len(lst)):
        lst[i] = lst[i].split(' ')#splits each line into seperate lists
    for i in range(len(lst)):
        for l in range(len(lst[i])):
            lst[i][l] = list(filter(str.isalnum, lst[i][l]))#checks if list is word and remove non letters
    return lst
def count_dict(lst):
    '''Takes list and return dict with sorted frequency and word'''
    new_dict = {}
    new_lst = []
    for i in range(len(lst)):
        for l in range(len(lst[i])):
            if len(lst[i][l]) > 3:#removes words not greater than 3
                new_lst.append(''.join(lst[i][l]).lower())#makes lower for count frequncey
    for i in range(len(new_lst)): #run through all lines 
        if new_lst[i] in new_dict:#checks if already in dict
            new_dict[new_lst[i]] += 1#adds one if in dict
        else:
            new_dict[new_lst[i]] = 1#adds key and sets value equal to 1
    value_sort = sorted(new_dict.values(), reverse=True) #Sorts values in descending order
    blank_dict = {}# new dict to place ordered keys and values
    for v in value_sort: # goes through all values in sorted
        for key in new_dict:# goes through all keys
            if v == new_dict[key]:
                blank_dict[key] = v#matches value to key and places in new dict
    return blank_dict #sorted word count dict
def words_once(dicts):
    ''' counts amount of words that are once'''
    count = 0#count starts at 0
    for i in dicts:
        if dicts[i] == 1:# add one once the value of the dict is one
            count +=1
    return count
if __name__ == "__main__":
    file_lst = get_file()
    dict_freq = count_dict(word_list(file_lst))
    once_words = words_once(dict_freq)
    print('{}{:>15}{:>25}'.format('#','Word', 'Freq.'))#title
    print('{:=>45}'.format('='))#seperator
    count = 0 # counts each word
    for i in dict_freq:
        if count < 9:
            count += 1
            print('{}{:>15}{:>25}'.format(count, i, dict_freq[i]))
        elif count < 10:#The ten is seperate to adjust for double digits
            count += 1
            print('{}{:>14}{:>25}'.format(count, i, dict_freq[i]))#adjust for double digits
    print('There are {} words that occur only once'.format(once_words))
    print('There are {} unique words in the document'.format(len(dict_freq)))

