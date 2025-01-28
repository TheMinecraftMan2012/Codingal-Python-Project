print("Choose your ride: ")
print("1. Car")
print("2. Bike")

choice_1 = int(input("Which one will you choose? (1 or 2): "))

if choice_1 == 1:
    print("Choose your car: ")
    print("1. Sedan Car")
    print("2. XUV Car")

    choice_2 = int(input("Which car will you choose? (1 or 2): "))

    if choice_2 == 1:
        print("You choosed Sedan Car")
    elif choice_2 == 2:
        print("You choosed XUV Car")
    else:
        print("Wrong Choice!")

elif choice_1 == 2:
    print("Choose your bike: ")
    print("1. Scooty")
    print("2. Scooter")

    choice_3 = int(input("Which bike will you choose? (1 or 2): "))

    if choice_3 == 1:
        print("You choosed Scooty")
    elif choice_3 == 2:
        print("You have choosed Scooter")
    else:
        print("Wrong Choice!")

else:
    print("Wrong Choice!")