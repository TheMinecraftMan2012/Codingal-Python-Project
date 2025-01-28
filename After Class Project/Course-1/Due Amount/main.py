def dueAmount(yourMoney):
    if yourMoney == 2500:
        print("Your Value is Balanced. No exchange.")

    elif yourMoney > 2500:
        return yourMoney - 2500
    
    else:
        print("Please put the right amount")
    
givenAmount = int(input("Your Bill is 2500. How much will you give?: "))

if givenAmount > 2500:
    print(f"You gave {givenAmount}. Now shopkeeper gave you {dueAmount(givenAmount)}.")

else:
    dueAmount(givenAmount)