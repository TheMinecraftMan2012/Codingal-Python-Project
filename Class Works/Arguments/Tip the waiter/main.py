def total_calc(bill, tip):
    total = bill * (1 + 0.01 * tip)
    print(f"Please pay total ${total}")

total_calc(150, 20)