a = int(input("Input a number: "))
n = int(input("Range for power: "))

for i in range(0, n):
    power = a**i
    sum = power + power
    print("The sum of %d powered numbers is %d" % (n, sum))