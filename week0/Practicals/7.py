def circularly_identical(list1, list2):
    list3 = list1 * 2
    for x in range(0, len(list1)):
        z = 0
        for y in range(x, x + len(list1)):
            if list2[z] == list3[y]:
                z += 1
            else:
                break
        if z == len(list1):
            return True
    return False


print("Input first list elements separated by space: ")
a = [int(x) for x in input().split()]
print("Input second list elements separated by space: ")
b = [int(x) for x in input().split()]
print(circularly_identical(a, b))
