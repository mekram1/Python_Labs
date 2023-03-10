# import required module
import os
# assign directory
path_of_the_directory = '/Users/dci-student/Desktop/AWS-ReStart-Python/AccessingFiles'
 
# iterate over files in
# that directory
for filename in os.listdir(path_of_the_directory):
    file = os.path.join(path_of_the_directory,filename)

    # checking if file is a directory
    if os.path.isfile(file):
        with open(file) as f:
            lines = f.readlines()
            #print(lines)
            data = ''.join(lines)
            new_str=data.replace("Re/Start","Python is Awesome")

            # only alnalyzes original files
            if("_pythonIsShit.txt" not in filename):
                with open(file.replace(".txt", "_pythonIsShit.txt"), 'w') as new_file:
                    new_file.write(new_str)

            print(data)
            data = ''.join(data.split())
            
                
        #data = f.read()

        #get the length of the data
        #number_of_characters = len(data)

        #print('Number of characters in text file :', number_of_characters)
        #print(f)