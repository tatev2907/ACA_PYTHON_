def isFactorial(n):
    i = 1
    while True:
        if n % i == 0:
            n //= i;
        else:
            break;
        i += 1;
    if n == 1:
        return True;
    else:
        return False;


def numb(n):
    t = True
    c = n + 1
    k = 2
    if c % 2 != 0:
        c += 1
    while t:
        if isFactorial(c):
            print(n, "Is a factorial of number")
            t = False
        else:
            c += k
    return k


m = int(input())
print(numb(m))
