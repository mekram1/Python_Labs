#Working with Conditionals
#Lab overview
#A section of code that compares two pieces of information is called a conditional statement. You can use conditionals to create different paths through the program. Using comparative operators, you will write a program that makes decisions.

#In this lab, you will:

                    #Use the if statement
                    #Use the else statement
                    #Use the elif statement
                    
#Use the input() function to get information from the user:
userReply = input("Do you need to ship a package? (Enter yes or no)")

#Use the if statement to print a response.
if userReply == "yes":
    print("We can help you ship that package!")

#Exercise 3: Working with the elif statement

# In this exercise, you will improve the Python script by offering 
# the user additional services. When you have multiple conditions, 
# you can use the elif statement, which is short for else-if.
#Note: The elif statement always comes after an if statement and before the else statement.

userReply = input("Would you like ot buy stamps, buy an envelope, or make a copy? (Enter Stamp, envelope, or copy) ")
if userReply == "stamps":
    print("we have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many evelope siyes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number)")
else:
    print("Thank you, please com again.")        
