# version 1
def second_max1(a):
    a.sort()
    # check if list element are not equal
    if max(a) != a[-2]:

        return a[-2]
    else:
        return 0.5


# version 2
def second_max2(b):
    mx = max(b[0], b[1])
    smx = min(b[0], b[1])
    n = len(b)
    for i in range(2, n):
        if b[i] > mx:
            smx = mx
            mx = b[i]
        elif b[i] > smx and mx != b[i]:
            smx = b[i]
        else:
            if smx == mx:
                smx = 0.5

    return smx


print("Input list elements separated by space: ")
c = [int(x) for x in input().split()]
print("Second max number is : ", second_max1(c))
# version 2
print("Second max number is : ", second_max2(c))
