fruits = ['apple', 'banana', 'cherry', 'pineapple', 'coconut']
a_list = []

for i in fruits:
    if "a" in i:
        a_list.append(i)

print("List without comprehension:", a_list)

b_list = [x for x in fruits if "a" in x]
print("List with comprehension:", b_list)