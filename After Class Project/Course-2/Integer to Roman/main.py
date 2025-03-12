class roman_conversion:
    def __init__(self, number):
        self.number = number
    
    def convert(self):
        if self.number >= 4000:
            print("Can't convert roman because number is equal to or greater than 4000")
        else:
            number = str(self.number)
            num_len = len(number)
            if num_len == 4:
                if number[0] == 1:
                    pass

conv = roman_conversion(int(input("Enter your number: ")))
conv.convert()