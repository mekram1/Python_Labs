# Import the libaries needed to export csv data
import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

#for key, value in myVehicle.items():
#    print("{} : {}".format(key,value))

myInventoryList = []
print("Inventory List with 0 cars:" + str(myInventoryList)) 

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',') 
    lineCount = 0 

    # Iterate over all rows
    for row in csvReader:
        print('')
        #print ("Current row " + str(lineCount) + ": " + str(row))

        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  

        else: 
            print("Current row object:" + str(row))
            #print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7] 
            #print ("Current Vehicle:" + str(currentVehicle))
            # puts vehicle into inventory list
            myInventoryList.append(currentVehicle) 
            print("Inventory List with {} cars:".format(lineCount) + str(myInventoryList)) 
            lineCount += 1  
            print('')
            
    print(f'Processed {lineCount} lines.')
    print('')

for carDictionary in myInventoryList:
    print("")
    #print(carDictionary)
    for keyIterator, valueIterator in carDictionary.items():
        print("{} : {} + Nancy {}".format(keyIterator,valueIterator, "Awesome"))
        print("-----")
    print("")
