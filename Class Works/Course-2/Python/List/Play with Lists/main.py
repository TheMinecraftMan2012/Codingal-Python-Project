L = [4, 6, 8, 25, 12, 1, 2]
print("Original List:", L)

count = 0

for i in L:
    count = count + i

avg = count/len(L)

print(f"Sum: {count}, Avarage: {avg}")

L.sort()

print("Serialized List:", L)
print("Smallest number:", L[0])
print("Largest number:", L[-1])