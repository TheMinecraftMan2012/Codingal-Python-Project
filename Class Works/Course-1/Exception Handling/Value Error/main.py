try:
    num = int(input("Enter a number: "))
    print(num)

except ValueError as ex:
    print("Exception: Please type a number, not a word or sentence")

print("I am outside of Try block")