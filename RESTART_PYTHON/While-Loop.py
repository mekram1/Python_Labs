print("Hello World")

# String to be analyzed
text= "I love learning python!"

# Splits the text into a list like ['I', 'love', 'learning', 'python!']
text_list=text.split()
print(text.split())

# Iterator being used to mange the While loop
i=0

# While loop iterates to the length of the list-1, due to the fact that array counters start at [0] 
while i<len(text_list):
    print(text_list[i])
    i+=1

# modifies the lists, and removes object on spot [0]
while 0<len(text_list):
    print(text_list.pop(0))

print("Our final List: "+ str(text_list))