class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    
    def __str__(self):
        return self.word + '(' + self.meaning + ')'

flash = []
print("Welcome to the flashcard application")

while True:
    word = input("Enter a word which will be added to flashcard: ")
    meaning = input("Enter the meaning of the word: ")

    flash.append(flashcard(word, meaning))
    option = int(input("Enter 0, If you want to make another flashcard. Otherwise, enter 1: "))

    if (option):
        break

for i in flash:
    print(">", i)