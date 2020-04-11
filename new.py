t=True

while t:
    s=input("Input your string")
    n=input("Input length")
    if not(n.isdigit()):
        print("Please insert a number for length")
        pass
    c=input("Input char")
    if len(c)>1:
        print("Please insert one symbol for fill")
        pass
    print(int(n))
    print(len(s))
    if int(n)>len(s):
        for i in range(int(n)):
            print("!!!!")
            print(c)
            s=s.join(str(c))
        t=False
print(s)