class reverse:
    def __init__(self, sentence: str):
        self.__sentence = sentence
        self.rev_sentence = ""
    
    def reverse_sentence(self):
        words = self.__sentence.split()
        reversed_words = words[::-1]
        self.rev_sentence = " ".join(reversed_words)
        print(self.rev_sentence)

sentence = "The Pizza is delicious"

obj = reverse(sentence)
obj.reverse_sentence()