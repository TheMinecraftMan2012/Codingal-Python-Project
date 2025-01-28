def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial doesn't exist in negative numbers")

else:
    print(f"The factorial of {num} is {factorial(num)}")