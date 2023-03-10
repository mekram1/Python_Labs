#List of values

x = [10, 20, 30, 40]
result = x[0] + x[1] + x[2] + x[3]

result_new = 0
for xi in x:
    print(xi)
    result_new = result_new + xi
    
    
N = len(x)
counter = 0
while counter < N:
    xi = x[counter]
    counter = counter + 1    
print("The result:", result_new)
