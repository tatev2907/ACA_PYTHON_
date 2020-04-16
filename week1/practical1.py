def implication3(a, b, c):
    return  not a or (not b or c)

def last_digit(number):
    if(number == 0):
        return 0
    else:
        return ((number * number) + last_digit(number - 1) )%10


def is_polyndrome(strr):
    listt = []
    for i in range(len(strr)):
        if (strr[i] in listt):
            listt.remove(strr[i])
        else:
            listt.append(strr[i])
    if (len(strr) % 2 == 0 and len(listt) == 0 or \
            (len(strr) % 2 == 1 and len(listt) == 1)):
        return True
    else:
        return False
print(is_polyndrome("ababb"))