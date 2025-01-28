try:
    age = int(input("Type your age: "))
    
    if age % 2 == 0:
        print("Your age is an even number")
    
    else:
        print("Your age is an odd number")

except ValueError:
    print("Error: Only numbers are allowed.")

except NameError:
    print("Error: Only numbers are allowed")