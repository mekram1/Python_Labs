#Enter first number
#Enter second number:
# Enter the operation: + , - ,*
#result: +

print("Enter first number:", end="")
x_input = input()
x = int(x_input)
#print("The first number is:", x)
#print("The type is:", type(x))
print("Enter the second number: ", end="")
y_input = input()
y = int(y_input)

print("Enter operation: ", end="")

operation = input()
# = means assign the right side to the left side
# == Check for equality
print("The operation is:, operation")
if operation == "+":
    result = x + y
elif operation == "-":
    result = x - y
elif operation == "*":
    result = x * x
elif operation == "/":
    result = x / y        
else:
    print("Invalid Number")
    exit(-1)
print(" The result: ", result)

print("The result of ", x, " and ", y, "is: ", x + y)