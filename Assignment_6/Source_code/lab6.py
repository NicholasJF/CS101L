########################################################################
##
## CS 101 Lab
## Program 6
## Name
## Email
##
## PROBLEM : Create  program that can encrypt and decrypt a string by moving the letters.
##
## ALGORITHM : 
##      1. Set up whle loop until they enter q to quit.
##      2. Create a function that will convert there string into a integer move the integer an entered amount of spaces then return it as a string.
##      3. Create a function that will convert there string into a integer move the integer the inverse of entered amount of spaces then return it as a string. This undoes the above step.
##      4. Create a function that shows a title and options to begin. The function returns the inputted value.
##      5. If  the option returned from above is one of the options either quit, encrypt, or decrypt. If not ask the above function again.
##      6. If they chose to encrypt ask for the text and how many spaces. These values will be run through the first function.
##      7. If they chose to dencrypt ask for the text and how many spaces. These values will be run through the second function.
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
def Encrypt(string_text, int_key): 
    '''Caesar-encrypts string using specified key.''' 
    string_text = string_text.upper()
    collection = list(string_text)
    for i in range(len(collection)): #to run through all characters in string
        if collection[i] != ' ': #ensure spaces are not replaced as shown in instructions
            collection[i] = chr((ord(collection[i])+ int_key - 65) % 26 + 65) #convert the entered number of spaces
    x = ''.join(collection) # put list back into single string
    return x
def Decrypt(string_text, int_key):
    '''Caesar-encrypts string using specified key.'''
    string_text = string_text.upper()
    collection = list(string_text)
    for i in range(len(collection)): #to run through all characters in string
        if collection[i] != ' ': #ensure spaces are not replaced as shown in instructions
            collection[i] = chr((ord(collection[i])- int_key - 65) % 26 + 65) #convert the entered number of spaces in inverse
    x = ''.join(collection) # put list back into single string
    return x
def Get_input():
    '''Interacts with user and shows menu. Returns any input.'''
    print('MAIN MENU:')
    print('1) Encode a string')#options
    print('2) Decode a string')
    print('Q) Quit')
    choice = input()
    return choice



  
  
def main(): 
  Again = True 
  while Again: 
    Choice = Get_input() 
    if Choice == '1': 
      Plaintext = input("Enter (brief) text to encrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Ciphertext = Encrypt(Plaintext, Key)
      print("Encrypted:", Ciphertext) 
      print()
    elif Choice == '2': 
      Ciphertext = input("Enter (brief) text to decrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Plaintext = Decrypt(Ciphertext, Key)
      print("Decrypted:", Plaintext) 
      print()
   
    elif Choice == 'Q' or Choice == 'q':  
        print('thanks for playing')
        Again = False 
    else:
        print('You need to choose a value of 1,2, or Q')
      
      
# our entire program: 
main() 
