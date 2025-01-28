string = input("Enter your own Word: ")
char = input("Enter your own character: ")

i = 0
count = 0

while (i < len(string)):
    if(string[i] == char):
        count += 1
    
    i += 1

print("The total number of times", char, "has occured =", count)