def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num

user_value = int(input("Enter a value: "))
print("Absolute value of %d is %d" % (user_value, absolute_value(user_value)))