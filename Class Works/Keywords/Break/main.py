a = input("Enter a word: ")

for i in a:
    if(i == "A" or i == "a"):
        print("Letter A found!")
        break

    else:
        print("Letter A not found")