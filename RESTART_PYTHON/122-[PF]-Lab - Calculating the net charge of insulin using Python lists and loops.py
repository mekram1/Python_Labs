#Calculating the Net Charge of Insulin by Using Python Lists and Loops
#Lab overview
#In the Flow Control module, you learned about if-else statements, while loops, lists, and for loops. Now you will apply what you have learned to the real-world application of human insulin.

#Here, you will use lists, for and while loops, and basic math to calculate the net charge of insulin from pH 0 to pH 14.

#In this lab, you will:

#Create a dictionary of pKa values (which indicate the strength of an acid) that will be used in the net charge calculations
#Use the count() method to get a count of amino acids
#Use a while loop to calculate the net charge of insulin from pH 0 to pH 14

#Exercise 1: Assigning variables, lists, and dictionaries
#From the navigation pane of the IDE, choose the file that you created in the previous Creating your Python exercise file section.

#Copy the following code, paste it into the file, and save the file:

# Python3.6  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin



pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

#Exercise 2: Using count() to count the numbers of each amino acid

#In this exercise, you will use the count() method and list 
#comprehension to count the number of Y, C, K, H, R, D, and 
#E amino acids. These amino acids contribute to the net charge.

insulin.count("Y")
float(insulin.count("Y"))
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
pH = 0
while (pH <=14):
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    print('{0:.2f}'.format(pH), netCharge)
    pH +=1
