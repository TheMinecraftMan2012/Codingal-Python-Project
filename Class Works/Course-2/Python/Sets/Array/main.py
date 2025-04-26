import array as arr

array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3, 4, 3])
print("Original array: " + str(array_num))

print("Frequency of 3 in array: " + str(array_num.count(3)))

array_num.reverse()
print("Reversed Array: " + str(array_num))