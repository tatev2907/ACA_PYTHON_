def all_positive(*args):
    return any([i < 0 for i in args])


def xor3(a, b, c):
    k = not (a and b) and (a or b)
    return not (k and c) and (k or c)


def mirror_string(s):
    s = list(s)
    for i in range(len(s)):
        p = ord(s[i])
        if p > 96 and p < 123:
            s[i] = chr(122 - (p - ord('a')))
        elif p > 64 and p < 91:
            s[i] = chr(90 - (p - ord('A')))
    return "".join(s)


def bit_concat(*args):
    val = [f'{i:08b}' for i in args]
    j = 8
    s = ''
    for i in val:
        s += (i[j - 2:j])
        j -= 2
    return int(s, 2)


def binary_sum(a, b):
    return int(a, 2) + int(b, 2)


def only_names(i):
    return not (i is None or i == "" or i.isdigit())


discriminant = lambda a, b, c: b * b - 4 * a * c
full_name = (lambda a, b: a + ' ' + b)
