

def getDoubleAlphabet(alphabet):
    #alphabet="ABC"
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

    
#Exercise 2: Encrypting a message
#The next function you define will request a 
#message to encrypt from the user.
#You will use the built-in function called input().

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

#Exercise 3: Getting a cipher key
#The cipher key is how far you will shift the letters. By 
# using two alphabets, you can have a cipher key that is 
# any integer from 1 to 25. Don’t count the key at index 26 
# because that key would shift you back to the original
# message.
#D#efine a function to request a cipher key from the user 
# by entering the following code:

def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount
#Exercise 4: Encrypting a message
#So far, the functions have been short and simple. That is usually the case when you keep to a specific task inside a function. The encryptMessage function will be a little longer.
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

#Exercise 5: Decrypting a message
#Functions are useful because you can reuse them. You will write a decryptMessage() function by reusing the encryptMessage() function. For this simple encryption, you can undo the encryption by shifting each letter back. Thus, instead of adding the cipher key, you will subtract the cipher key. To avoid rewriting most of the logic, you will pass in a negative cipher key.

#Next, enter the following code, and save the file:

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

#Exercise 6: Creating a main function
#You have built a collection of user-defined functions that will help you write a Caesar cipher program. The main logic of the program will, of course, also be contained in a function.

#Before you look at the code, plan out your logic:
#Define a string variable to contain the English alphabet.
#To be able to shift letters, double your alphabet string.
#Get a message to encrypt from the user.
#Get a cipher key from the user.
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
    
    
    print()
    
    runCaesarCipherProgram()
    
    