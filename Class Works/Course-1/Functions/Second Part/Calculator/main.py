def add(P, Q):
    return P + Q

def subtract(P, Q):
    return P - Q

def divide(P, Q):
    return P / Q

def multiply(P, Q):
    return P * Q

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("Operators")
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")

op = input("Which one will you choose?: ")

print("First Number is:", num1)
print("Second Number is:", num2)
print("Selected Operator:", op)

if op == "A" or op == "a":
    print("The Result is", add(num1, num2))

elif op == "B" or op == "b":
    print("The Result is", subtract(num1, num2))

elif op == "C" or op == "c":
    print("The Result is", divide(num1, num2))

elif op == "D" or op == "d":
    print("The Result is", multiply(num1, num2))