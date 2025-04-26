class IOString:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Enter String: ")
    
    def print_string(self):
        print("Your word is:", str(self.string).upper())

obj = IOString()
obj.get_string()
obj.print_string()