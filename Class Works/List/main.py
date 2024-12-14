lst = ['Apple', 'Banana', 'Coconut', 'Mango', 'Kiwi']

print("Length of list", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('Guava')
print("Updated List:", lst)

lst.remove('Kiwi')
print("Updated List:", lst)

lst.sort()
print("Updated List:", lst)

lst.pop(1)
print("Updated List: ", lst)

lst.reverse()
print("Updated List:", lst)

print("\n")
print("Multiplication On list:", lst * 2)

print("Sliced List: ", lst[0:4])