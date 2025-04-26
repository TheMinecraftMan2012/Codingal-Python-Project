class Bangladesh:
    def capital(self):
        print("Dhaka is the capital of Bangladesh")
    
    def language(self):
        print("Bangla is most widely spoken language of Bangladesh")
    
    def type(self):
        print("Bangladesh is a developing country")

class India:
    def capital(self):
        print("New Delhi is the capital of India")
    
    def language(self):
        print("Hindi is most widely spoken language of India")
    
    def type(self):
        print("India is a developing country")

class USA:
    def capital(self):
        print("Washingtion is the capital of USA")
    
    def language(self):
        print("English is most widely spoken language of USA")
    
    def type(self):
        print("USA is a developed country")

obj_bd = Bangladesh()
obj_ind = India()
obj_usa = USA()

for country in (obj_bd, obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()