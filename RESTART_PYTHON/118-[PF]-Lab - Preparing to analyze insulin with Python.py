#Preparing to Analyze Insulin with Python
#Lab overview
#In information technology, Python works well as the programming 
# language of choice for manipulating strings, sequences, and numbers.
# Python is especially preferred in scientific computing applications 
# such as physics, chemistry, and biology.

#In some of the labs for the Python modules, you will perform simple 
# sequence manipulations and calculations on human insulin, which is a 
# well-known hormone in the human body that is responsible for 
# regulating sugars.

#In this lab, you will:

#Retrieve the protein sequence of human insulin from human 
# preproinsulin


#Exercise 1: Retrieving the protein sequence of human preproinsulin
#The National Center for Biotechnology Information (NCBI) has 
#information on many biological sequences.

#In the AWS Cloud9 IDE, on the navigation pane, choose 
#File > New File and 
#save the file as preproinsulin-seq.txt.


#Exercise 2: Obtaining the protein sequence of human insulin
#Insulin is obtained from preproinsulin through a series of cut-and-paste procedures. Preproinsulin contains a 24aa signal sequence and an 86aa proinsulin molecule. Amino acids 25–54 and amino acids 90–110 are the processed insulin molecule. Use Python, Bash, or manual manipulation to retrieve only those amino acids in the sequence that compose insulin.
#Manually or programmatically delete ORIGIN, 1, 61, //, and the spaces and return carriages.

#In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as preproinsulin-seq-clean.txt.

#In the file preproinsulin-seq-clean.txt, copy your results.

#Confirm that your file has 110 characters of lowercase letters, which represent the amino acids in the sequence of human preproinsulin.

#In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as lsinsulin-seq-clean.txt.

#In lsinsulin-seq-clean.txt, save amino acids 1–24. Verify that your file has 24 characters.

#In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as binsulin-seq-clean.txt.

#In binsulin-seq-clean.txt, save amino acids 25–54. Verify that your file has 30 characters.

#In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as cinsulin-seq-clean.txt.

#In cinsulin-seq-clean.txt, save amino acids 55–89. Verify that your file has 35 characters.

#In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as ainsulin-seq-clean.txt.

#In ainsulin-seq-clean.txt, save amino acids 90–110. Verify that your file has 21 characters.

# import required module
import os
# assign directory
path_of_the_directory = '/Users/dci-student/Desktop/AWS-ReStart-Python/118-[PF]-Lab - Preparing to analyze insulin with Python.py'
 
# iterate over files in
# that directory
for filename in os.listdir(path_of_the_directory):
    print(filename)
    file = os.path.join(path_of_the_directory,filename)
    print("File of os" + str(file))
    if os.path.isfile(file):
        with open(file) as f:
            lines = f.readlines()
                #print(lines)
            data = ''.join(lines)
            print(data)
            #print('')
            #print('File Name =',f.name)
            #print('lines =',len(lines))
            #print('Words = ',len(data.split()))
            #data = ''.join(data.split())
            #print('characters = ',len(data))
            #print('')
                #read the content of file
        #data = f.read()

        #get the length of the data
        #number_of_characters = len(data)

        #print('Number of characters in text file :', number_of_characters)
        #print(f)