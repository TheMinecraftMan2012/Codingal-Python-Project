a = int(input("Enter the base for powers: "))
n = int(input("Enter the range point of power: "))

for i in range(1, n + 1):
    power = a**i
    print("{0} to the power {1} is {2}".format(a, i, power))