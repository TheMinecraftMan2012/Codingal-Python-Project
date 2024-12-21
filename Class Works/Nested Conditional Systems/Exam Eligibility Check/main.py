medical_cause = input("Do you have medical issues? (Y / N): ")
attendence = int(input("Enter the attendence of your student: "))

if medical_cause == "Y":
    print("You are allowed")

else:
    if attendence >= 75:
        print("You are allowed")
    else:
        print("You are not allowed")