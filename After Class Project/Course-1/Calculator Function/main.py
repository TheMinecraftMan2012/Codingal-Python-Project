while True:
    first_num = int(input("Enter First Number: "))
    second_num = int(input("Enter Second Number: "))
    operator = input("Enter Operator(+, -, /, *): ")

    def add(num1, num2): print("Result is ", num1 + num2)
    def sub(num1, num2): print("Result is ", num1 - num2)
    def mul(num1, num2): print("Result is ", num1 * num2)
    def div(num1, num2): print("Result is ", num1 / num2)

    if operator == "+": add(first_num, second_num)
    elif operator == "-": sub(first_num, second_num)
    elif operator == "*": mul(first_num, second_num)
    elif operator == "/": div(first_num, second_num)