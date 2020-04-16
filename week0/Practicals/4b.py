def fact(n):
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return "does not exist for negative numbers"
    else:
        return n * fact(n - 1)


num = int(input("Input number: "))
print("Factorial of", num, "is", fact(num))
