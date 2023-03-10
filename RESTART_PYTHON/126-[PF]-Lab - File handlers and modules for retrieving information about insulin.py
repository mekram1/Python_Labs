#Lab overview
#In this lab, you will:

#Create a module
#Open a file and load the JSON data it contains using the 
# built-in JSON module of Python
#Parse the JSON structure to access insulin data
#Calculate the rough molecular weight of human insulin using
# given code (similar to the lab Working with the String 
# Sequence and Numeric Weight of Insulin in Python)

#Exercise 1: Creating the JSON molecules data file


import json
def readJsonFile(insulin.json):
    
    data=""
    
def readJsonFile(insulin.json):
    data =""
    with open('AWS-RESTART-PYTHON/insulin.json') as json_file:
        data = json.load(json_file)
    return    
   
import json
def readJsonFile(insulin.json):        
    data = ""
    try:
        with open(insulin.json) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data

