rows = int(input("Please enter the number of rows: "))
number = 1

print("Flyod's triangle")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end=' ')
        number += 1
    
    print()