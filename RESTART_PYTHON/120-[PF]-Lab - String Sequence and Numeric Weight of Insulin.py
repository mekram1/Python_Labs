#Working with the String Sequence and Numeric Weight of Insulin in Python
#Lab overview
#In the Python Basics module, you learned about variables, comments, math, concatenations, and exceptions. Now, you will apply what you have learned to the real-world application of human insulin.

#You will store the protein sequence of human preproinsulin in a string variable and the weight of preproinsulin in int and float variables. Next, you will print these variables to the console, with comments that explain the code. You will do basic math and string concatenations.

#In this lab, you will:

#Add comments that explain the intention and flow of your code
#Use print() to print elements of your Python code to the console
#Use string manipulations to get the sequence of insulin from preproinsulin
#Do basic math on the molecular weight and sequence of insulin
#Assign string, int, and float variables to numbers that represent the weight of insulin
#Explore Python exceptions

#Exercise #1: Assigning variables to the sequence elements of human insulin
#In this exercise, you will create variables and assign a string 
# value to them.

# Store the human preproinsulin sequence in a variable called preproinsulin:

preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:

lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

#Exercise 3: Using print() to display sequences of human insulin to the console
#In this exercise, you will use the print() built-in method to display sequence elements of human insulin in the console.

#Write a note on the next line:

# Printing "the sequence of human insulin" to console using successive print() commands:

print("The sequence of human preproinsulin:")
# Printing to console using concatenated strings inside the print function (one-liner):

print("The sequence of human insulin, chain a:" + aInsulin)

print("The sequence of human insulin, chain, aInsulin")


#Exercise 4: Calculating the rough molecular weight of human insulin using the given code
#In this lab, you will calculate the molecular weight of insulin, which you will work with in later labs.

#Ensure that your .py file is open
#Copy the following code, and at the end of the .py file, paste it.

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  
# Count the number of each amino acids  
aaCountInsulin = ({x: float(aInsulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  
# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))

molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
