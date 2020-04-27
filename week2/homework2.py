from collections import defaultdict
def bisect_position(a, x):
    ind = 0
    l = len(a)
    while ind < l:
        list_midle = (ind + l) // 2
        if x < a[list_midle]:
            l = list_midle
        else:
            ind = list_midle + 1
    return ind


def all_sum(a: int) -> list:
    return [[i, a - i] for i in range(1, a // 2 + 1)]


def duplicate_characters(st1):
    st1 = st1.replace(" ", "")
    d = defaultdict(int)
    i = 0
    s = set()
    for k in st1:
        d[k] += 1
    p = list(d.keys())
    for v in d.values():
        if v > 1:
            s.add(p[i])
        i += 1
    return s


def compare_lists(ls1: list, ls2: list) -> bool:
    if len(ls1) != len(ls2):
        return False
    k = [x for x in ls1 if x in ls2]
    return len(k) == len(ls1)


def heapify(arr, n, k):
    root = k
    l = 2 * k + 1
    r = 2 * k + 2
    if l < n and arr[k] < arr[l]:
        root = l
    if r < n and arr[root] < arr[r]:
        root = r
    if root != k:
        arr[k], arr[root] = arr[root], arr[k]
        heapify(arr, n, root)


def heapq(lst, number):
    lst.append(number)
    n = len(lst)
    for i in range(n, -1, -1):
        heapify(lst, n, i)
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]  # swap
        heapify(lst, i, 0)
    return lst


def sort_list(lst1, st1=None):
    n = len(lst1)
    if n == 0 or n == 1:
        return lst1
    i = 0
    while (i < n - 1):
        j = n - 1
        while (j > i):
            if (lst1[j] < lst1[j - 1]):
                lst1[j - 1], lst1[j] = lst1[j], lst1[j - 1]
            j -= 1
        i += 1
    if st1 == 'ascending' or st1 == None:
        return lst1
    elif st1 == 'descending':
        lst1.reverse()
        return lst1
    else:
        print("Input correct ordering type:")
