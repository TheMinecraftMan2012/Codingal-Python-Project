sq_list = []
odd_sq_list = []
even_sq_list = []

min_value = int(input("Enter min value: "))
max_value = int(input("Enter max value: "))

for i in range(min_value, max_value + 1):
    sq_values = i ** 2
    sq_list.append(sq_values)

print("Your square List:", sq_list)

for j in sq_list:
    if j % 2 == 0:
        even_sq_list.append(j)
    else:
        odd_sq_list.append(j)


print("Odd Square List:", odd_sq_list)
print("Even Square List:", even_sq_list)