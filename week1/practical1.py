def implication3(a, b, c):
    return  not a or (not b or c)

def last_digit(number):
    if(number == 0):
        return 0
    else:
        return ((number * number) + last_digit(number - 1) )%10