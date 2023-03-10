#Working with Loops
#Lab overview
#A loop is a segment of code that repeats. You will be introduced to two types of loops: the while loop and the for loop.

#In this lab, you will:

            #Use a while loop
            #Use a for loop
            
#Exercise 1: Working with a while loop

#A while loop makes a section of code repeat until a certain 
#condition is met. In this exercise, you will create a Python 
#script that asks the user to correctly guess a number.

#Printing the game rules
#Use the print() function to inform the user about your game:

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#Importing random and writing a while loop

#You will use the import command to include code that someone else 
# wrote. Up to now, you have been using built-in functions. 
# Recall that a function is a piece of reusable code.

#At the top of the file, include the Python module
# (which is a type of library) called random.

import random

#Place the cursor on the next line after the second print() 
# statement. Next, enter a statement that will generate a random 
# number between 1 and 10 by using the randint() function of the
# random module.

number = random.randint(1,10)
#creating a variable called isGuessRight:
isGuessRight = False

#To handle the game logic, create a while loop:
while isGuessRight !=True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!" .format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))
        
#Note: 
# The while loop will repeat the code inside the loop until the 
#number is guessed correctly, which is represented by the condition
#isGuessRight != True in the code. Additionally, Python uses 
#indentation to determine logic blocks, or what statements are 
#considered to be part of the while loop. You can indent a line 
#by placing the cursor next to a statement and pressing TAB.           

#Writing pseudocode
#Before you run the Python script, write out the logic of the while loop in written (non-code) sentences. This technique is called pseudocoding.

#For example:
#If the user has not guessed the correct answer, enter the loop.
#Ask the user for a guess.
#Is the guess the correct number?
#If the correct guess, tell the user it was the correct guess and exit the loop.
#If the wrong guess, tell the user it was the wrong guess and continue the loop.

#To inform the user about your script, use the print() function:

print("Count to 10!")

#Writing the for loop
#In Python, you can include a large amount of functionality in a few 
# words. This feature makes Python relatively easy to write compared 
# to other programming languages, but it can also make Python code 
# more difficult to read. In this activity, you will use the for 
# statement, but you will also spend some time analyzing it after 
# you see it run.

#Return to the Python script. To count to 10, enter the following code.



#Note: 
# Python uses indentation to determine that the print statement 
# is inside the for loop statement.):

for x in range (0, 11):
    print(x)