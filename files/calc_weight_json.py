#Exercise 3: Creating the main program
#You create the main program that parses the JSON data and 
#calculates the molecular weight as you did in a previous lab. 
import jsonFileHandler
data = jsonFileHandler.readJsonFile('files/insulin.json')

#Test if the returned data is not empty and obtain the insulin data.           
if data != "" :
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
else:
    print("Error. Exiting program")