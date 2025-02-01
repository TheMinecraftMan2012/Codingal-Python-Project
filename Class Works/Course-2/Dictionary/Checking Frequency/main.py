test_dict = {'key1': 2, 'key2': 2, 'key3': 2, 'key4': 2, 'key5': 1}

K = 2
freq = 0

for i in test_dict:
    if test_dict[i] == K:
        freq += 1

print("Frequency of K: " + str(freq))