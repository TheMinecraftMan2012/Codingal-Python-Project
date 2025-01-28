word = input("Enter a word to reverse: ")
word2 = ('')

for i in word:
    word2 = i + word2

print("Your Original Word:", word)
print("Your Reversed Word:", word2)