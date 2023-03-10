#Enter number: 10, 20, 30

print("Enter numbers: ", end="")
numbers_input = input()

"10, 20, 30" #make string to list of integer
[10,20,30]
split_numbers = numbers_input.split(",")

#first_number = split_numbers[0]
#first_number_stripped = first_number.strip() #strip() remove any whitespaces

#n1 = int(first_number_stripped)




#second_number = split_numbers[0]
#second_number_stripped = second_number.strip() #strip() remove any whitespaces
#n2 = int(second_number_stripped)


result = 0
for number in split_numbers:
    xi = int(number.split())
    result = result + xi
    print("Current result =", )
    
print("The input was: ", result)

