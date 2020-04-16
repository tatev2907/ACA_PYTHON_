def fun_c(a):
    for num in a:
        res = [int(x) for x in str(num)]
        b = set(res)
        if len(b) == len(res):
            return num
    return "-1"


print("Input list elements separated by space: ")
inp = [int(x) for x in input().split()]
print(fun_c(inp))
