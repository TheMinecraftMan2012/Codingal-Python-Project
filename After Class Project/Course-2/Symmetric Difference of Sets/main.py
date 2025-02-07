A = {1, 2, 3}
B = {3, 4, 5, 6}

x = A - B
y = B - A

sym_diff = x.union(y)
print(sym_diff)