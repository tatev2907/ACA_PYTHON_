s = input("input string: ")
n = len(s) // 2
t = True #simetric e te voch
i = 0
for j in range(len(s) - 1, n -1, -1): #sksvac toxi verjic minchev toxi kes stugum enq
    if not t : #ete simetrik che durs gal ciklic
        break
    if s[i] != s[j]:
        t = False
    i += 1
if not t:
    print("False")
elif i >= n:
    print("True")
