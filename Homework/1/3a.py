s = input("input string: ")
n = len(s) // 2
t = True
i = 0
for j in range(len(s) - 1, len(s) // 2 - 1, -1):
    if not t or i == len(s) // 2:
        break
    if s[i] != s[j]:
        t = False
    i += 1
if not t:
    print("False")
elif i == len(s) // 2:
    print("True")
