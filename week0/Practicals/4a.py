def fact1(num):
    factorial = 1
    if num < 0:
        return "Does not exist for negative numbers"
    elif num == 0:
        return "1"
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
    return factorial


num2 = int(input("Input number: "))
print("Factorial ", num2, "-> ", fact1(num2))
