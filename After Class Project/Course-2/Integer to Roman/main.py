class roman_conversion:
    def __init__(self, number):
        self.number = number
    
    def convert(self):
        if self.number <= 0 or self.number >= 400:
            return "Invalid: Roman number can convert 1 to 3999"
        else:
            roman_numerals = {
            1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
            90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"
            }
    
            roman_str = ""
            for value in sorted(roman_numerals.keys(), reverse=True):
                while self.number >= value:
                    roman_str += roman_numerals[value]
                    self.number -= value
            return roman_str

num = int(input("Enter your number: "))
conv = roman_conversion(num)
print(conv.convert())