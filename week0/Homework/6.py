def gcb(x, y):
    if y != 0:
        if x > y:
            return gcb(y, x % y)
        elif x < y:
            return gcb(x, y % x)
    return x
a = int(input("Input first number: "))
b = int(input("Input second number: "))
print(gcb(a, b))
