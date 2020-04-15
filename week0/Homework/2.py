input_string = input("Enter a list elements separated by space: ")
a = input_string.split()
for x in a:
    n=a.count(x)
    if n > 1:
        for i in range(n-1):
            a.remove(x)
print(a)