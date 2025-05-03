test_dic = {
    'py': 4,
    'cpp': 4,
    'c': 4,
    'html': 4,
    'css': 5,
    'js': 5,
    'java': 5,
    'json': 5,
    'h': 5,
    'pyi': 2,
    'pyw': 1
}

A = 4
B = 5

freq4 = 0
freq5 = 0

for i in test_dic:
    if test_dic[i] == A:
        freq4 += 1
    elif test_dic[i] == B:
        freq5 += 1

print("Frequency of 'A': " + str(freq4))
print("Frequency of 'B': " + str(freq5))