tupleX = (2, 4, 6, 8, 9, 10)
tupleY = ()

print("This your tuple:", tupleX)
n = int(input("What number will you multiply with them: "))

for i in range(6):
    multiplied_value = tupleX[i] * n
    tupleY = tupleY + (multiplied_value, )

print("Your multiplied tuple:", tupleY)