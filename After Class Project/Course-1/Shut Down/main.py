import sys
import time

def shutdown(TrueOrFalse):
    if TrueOrFalse:
        print("Shutting Down your shop.....")
        time.sleep(5)
        sys.exit()
    else:
        sys.exit()

print("It is 8 pm")
light = input("Do you want to turn on lights? (Y/N):")

if light == "y" or light == "Y":
    print("Turned on lights")

elif light == "n" or light == "N":
    print("You are in dark")

else:
    print("Wrong Choice")
    time.sleep(3)
    sys.exit()

print("It's 10pm")
print("All shops are closing.")
ClOrOp = input("Will you close your shop?(Y/N): ")

if ClOrOp == "Y" or ClOrOp == "y":
    shutdown(True)

elif ClOrOp == "N" or ClOrOp == "n":
    shutdown(False)

else:
    print("Wrong Choice")
    time.sleep(3)
    sys.exit()