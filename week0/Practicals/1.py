def isVowel(c):
    vowels = ['a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'I', 'U']
    if c in vowels:
        return True
    return False


def rev_vowels(s):
    i = 0
    j = len(s) - 1
    s = list(s)
    while (i < j):
        if not isVowel(s[i]):
            i += 1
            continue
        if not isVowel(s[j]):
            j -= 1
            continue
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return "".join(s)


string1 = input("Inpur string: ")
print(rev_vowels(string1))
