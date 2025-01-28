try:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    result = num1 / num2
    print("The result is", result)

except ZeroDivisionError:
    print("Error: Can't divide by zero!")

except ValueError:
    print("Error: Enter only number, not a word!")

except NameError:
    print("Error: Only typing numbers are allowed!")

except:
    print("Error: Something is wrong, please try again later.")

finally:
    print("I will excecute no matter what happens")