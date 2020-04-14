def func(inp_s):
    sum_of_digits = sum(int(digit) for digit in inp_s)
    return sum_of_digits
inp = input("Input number: ")
print(func(inp))