age = int(input("Enter your age: "))

if age < 10:
    print("You're below 10. You are not allowed.")

elif age >= 10 and age <= 20:
    print("You're allowed.")

else:
    print("You're over 20. You're not allowed.")