#Lab overview
#In programming, a function is a named section of a program 
# that performs a specific task. Python has built-in 
# functions like print() that are provided by the language. 
# Additionally, you can use functions provided by other 
# developers through the import statement. For example, 
# you can use import math if you want to use the math.floor()
# function. In Python, you can make your own functions, 
# which are called user-defined functions.

#To drive the discussion of user-defined functions, you will
# write a program that implements a Caesar cipher, which is 
# a simple method of encryption. A Caesar cipher takes the 
# letters of a message and shifts each letter along the 
# alphabet by a certain number of places.

#In this lab, you will:

#Create user-defined functions
#Use several functions to implement a Caesar cipher encryption 
# program

#Exercise 1: Creating a user-defined function
#To start the process of implementing a Caesar cipher in
# Python, you will create a simple user-defined function.

#Creating your Python exercise file
#From the menu bar, choose File > New From Template > Python File.
#This action creates an untitled file.
#Delete the sample code from the template file.
#Choose File > Save As..., provide a suitable name 
# for the exercise file (for example, caesar-cipher.py), 
# and save it under the /home/ec2-user/environment directory.
#import math
#math.cipher


def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
print(getDoubleAlphabet("alphabet"))

#Exercise 2: Encrypting a message
#The next function you define will request a message to 
#encrypt from the user. You will use the built-in 
#function called input().

#In the text editor, enter the following code, and save the file:
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
print(getMessage())

#Exercise 3: Getting a cipher key
#The cipher key is how far you will shift the letters. 
#By using two alphabets, you can have a cipher key that 
#is any integer from 1 to 25. Don’t count the key at 
#index 26 because that key would shift you back to the 
#original message.

#Define a function to rHelloequest a cipher key from the 
# user by entering the following code:
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount

print(getCipherKey())

#Exercise 4: Encrypting a message
#So far, the functions have been short and simple. 
# That is usually the case when you keep to a specific 
# task inside a function. The encryptMessage function
# will be a little longer.

#Before writing the code, you should plan out the algorithm for encryption as follows:
#Take three arguments: the message, the cipherKey, and the alphabet.
#Initialize variables.
#Use a for loop to traverse each letter in the message.
#For a specific letter, find the position.
#For a specific letter, determine the new position given the cipher key.
#If current letter is in the alphabet, append the new letter to the encrypted message.
#If current letter is not in the alphabet, append the current letter.
#Return the encrypted message after exhausting all the letters in the message.

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

#encryptedMessage = input("encryptedMessage: " )
#print(encryptMessage)
#uppercaseMessage = input("Uppercase:")



#Exercise 5: Decrypting a message
#Functions are useful because you can reuse them. You will write a decryptMessage() 
# function by reusing the encryptMessage() function. For this simple encryption, 
# you can undo the encryption by shifting each letter back. Thus, instead of adding 
# the cipher key, you will subtract the cipher key. To avoid rewriting most of the logic,
# you will pass in a negative cipher key.

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)


#Exercise 6: Creating a main function
#You have built a collection of user-defined functions that will help you write a Caesar cipher program.
# The main logic of the program will, of course, also be contained in a function.
#Before you look at the code, plan out your logic:
#Define a string variable to contain the English alphabet.
#To be able to shift letters, double your alphabet string.
#Get a message to encrypt from the user.
#get a cipher key from the user.
#Encrypt the message.
#Decrypt the message.

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    
    myMessage = getMessage()
    print(myMessage)
    
    myCipherKey = getCipherKey()
    print(myCipherKey)
    
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    
    runCaesarCipherProgram()
    
                    # The Output 
   # Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
#Alphabet2: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
#Please enter a message to encrypt: new message
#new message
#Please enter a key (whole number from 1-25): 4
#4
#Encrypted Message: RIA QIWWEKI
#Decypted Message: NEW MESSAGE