num = int(input("Enter a number to check: "))
flag = False

for i in range(2, num):
    if (num % i == 0):
        flag = True
        break

if flag:
    print("%d is not a prime number" % num)

else:
    print("%d is a prime number" % num)