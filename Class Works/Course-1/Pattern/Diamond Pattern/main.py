rowSize = int(input("Enter the number of rows: "))

if (rowSize % 2 == 0):
    halfDiamondRow = int(rowSize / 2)
else:
    halfDiamondRow = int(rowSize / 2) + 1

space = halfDiamondRow - 1

for i in range(1, halfDiamondRow + 1):
    for j in range(1, space + 1):
        print(end = " ")
    
    space -= 1
    num = 1
    
    for j in range(2 * i - 1):
        print(end = str(num))
        num += 1

    print()

space = 1

for i in range(1, halfDiamondRow):
    for j in range(1, space + 1):
        print(end = " ")
    
    space += 1
    num = 1
    
    for j in range(1, 2 * (halfDiamondRow - i)):
        print(end = str(num))
        num += 1

    print()