#### ----------------- Input -----------------
### Ekram ####
print("")
print("--------")
print("Child Age")
print("--------")

# input is currently commented out, when required put it back in
age = 8 # int(input("What is your age? "))

if age >= 18:
    print("adult")

elif age < 18 and age >=16:
    print("teenager allowed to drink beer")

elif age < 16 and age >=13:
    print("teenager not allowed to drink beer")

else:
    print("child")


#### ----------------- LIST -----------------
list_students = ["Alice", "Bob", "Charly"]
student_count = len(list_students)

print("Student count: " + str(student_count))

#### ----------------- WHILE -----------------
print("")
print("----------")
print("WHILE LOOP")
print("----------")

# runner variable, required to iterate through the lisrt
i= 0
while i<student_count:
    print("iteration no. "  + str(i))
    print("Student is " + str(list_students[i]))
    i+=1

#### ----------------- FOR -----------------
print("")
print("--------")
print("FOR LOOP")
print("--------")

for x in list_students:
    print("Student is " + str(x))

#### ----------------- Dictionary -----------------
# store name as key
# store age as value
student_dict = {"Thomas":12, "Katherina":14, "Sophie":17}

print("")
print("----------")
print("Dictionary")
print("----------")
# print("Age of Thomas: " + str(student_dict.get("Thomas")))
# print("Age of Katherina: " + str(student_dict["Katherina"]))

# key -> name
# value -> age
for key, value in student_dict.items():
    print("Age of {}: ".format(key) + str(value))

#### ----------------- Function -----------------
print("")
print("----------")
print("Function")
print("----------")

def insertStudent(student):
    student_dict.update(student)
    return student_dict

# store name as key
# store age as value
student_dict = {"Thomas":12, "Katherina":14, "Sophie":17}

daniel = {"Daniel":28}
andrea = {"Andrea":34}

# Function call
insertStudent(daniel)
insertStudent(andrea)
insertStudent({"Tim":34})
insertStudent({"Tom":34})
insertStudent({"Jerry":34})

for key, value in student_dict.items():
    print("Age of {}: ".format(key) + str(value))


a=1
b=2
c=3

d=4
e=5
f=6

def adding(x,y,z):
    Result=x+y+z
    return Result

print("")
print("----------")
print("Simple Add function")
print("----------")

# Function Call
print(adding(a,b,c)+adding(d,e,f))