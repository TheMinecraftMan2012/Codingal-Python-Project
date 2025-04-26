# --- Zipping Sets --- #

s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))

print(s3, "\n")

# --- Zipping Lists --- #

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

# --- Zipping List to Dictionary --- #

stocks = ["IPhone", "Keyboard", "CPU"]
prices = [85000, 5000, 75000]

new_dict = {
    stocks: prices for stocks, prices in zip(stocks, prices)
}

print("\n{}".format(new_dict))