import math

n = int(input("Input a range: "))

print("Here is the power series with range of", str(n))
for i in range(1, n + 1):
    power = math.pow(i, i)
    print(power)