#Lab overview
##In Python, string and numeric data types are often used in groups called collections. Three such collections that Python supports are the list, the tuple, and the dictionary.

#In this lab, you will:

                    #Use the list data type
                    #Use the tuple data type
                    #Use the dictionary data 

#Defining a list
#In this activity, you will edit a Python script to hold a collection of fruit names, or a list of fruit.

myFruitList = ["apple" , "banana" , "cherry"]
print(myFruitList)
print(type(myFruitList))

#Accessing a list by position
#You can access the contents of a list by position. In this activity, you will print out each item in our list by their position:
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])



#Changing the values in a list
#The values of a list can be changed. In this activity, you will change cherry to orange.
myFruitList[2] = "orange"
print(myFruitList)

#Exercise 2: Introducing the tuple data type

#Defining a tuple
#The tuple is like a list, but it can't be changed. A data type that can't be changed after it's created is said to be immutable. To define a tuple, you use parentheses instead of brackets ([]).

#Create a tuple by entering the following code:
myFinalAnswerTuple = ("apple", "banana" , "Pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#Accessing a tuple by position
#Like a list, the items of a tuple can also be accessed by position:

#To access the apple string, Banana String and Pineapple string, enter the following code:
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#Exercise 3: Introducing the dictionary data type
#Defining a dictionary
#A dictionary is a list with named positions (keys). Imagine that your list shows people’s favorite fruit.

#Return to the Python script, and enter the following code:
myFavoriteFruitDicktionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo" : "pineapple"
}
    #Use the print() function to write the dictionary to the shell:
    #Use the type() function to write the data type to the shell:
print(myFavoriteFruitDicktionary)
print(type(myFavoriteFruitDicktionary))
