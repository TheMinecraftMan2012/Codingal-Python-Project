name = "Raaeid"
age = 12
is_student = True
weight = 60.5

print("Name: ", name)
print("The datatype of name is ", type(name))
print("Age: ", age)
print("The datatype of age is ", type(age))
print("Is student?: ", is_student)
print("The datatype of 'is_student' is ", type(is_student))
print("Weight: ", weight)
print("The datatype of weight is ", type(weight))

print("\n After Type Casting...")
age = str(age)
print("The age is now ", type(age))
weight = int(60.5)
print("The weight is now ", type(weight))