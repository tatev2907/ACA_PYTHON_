def implication3(a, b, c):
    return not a or (not b or c)


def last_digit(number):
    if (number == 0):
        return 0
    else:
        p = 1
        for i in range(2, number + 1):
            p = (p % 10 + (i * i) % 10) % 10
        return p


def is_polyndrome(strr):
    listt = []
    for i in range(len(strr)):
        if (strr[i] in listt):
            listt.remove(strr[i])
        else:
            listt.append(strr[i])
    if (len(strr) % 2 == 0 and len(listt) == 0 or (len(strr) % 2 == 1 and len(listt) == 1)):
        return True
    else:
        return False


def recursive_or(list1):
    return any([list1[i] or recursive_or(list1[i + 1:]) for i in range(len(list1))])


def quic_or(list1):
    return list1.count(True) > 0


def expr_value(exp):
    exp = list(exp)
    if (len(exp) == 0):
        return -1
    i = 0
    while '*' in exp or '/' in exp:
        opd1 = float(exp[i])
        opr = (exp[i + 1])
        opd2 = float(exp[i + 2])
        if (opr == '*'):
            exp[i] = opd1 * opd2
            exp = exp[:i + 1] + exp[i + 3:]
            i = 0
        elif (opr == '/'):
            exp[i] = opd1 / opd2
            exp = exp[:i + 1] + exp[i + 3:]
            i = 0
        else:
            i += 2
    i = 0
    while len(exp) != 1:
        opd1 = float(exp[i])
        opr = (exp[i + 1])
        opd2 = float(exp[i + 2])
        if (opr == '+'):
            exp[i] = opd1 + opd2
            exp = exp[:i + 1] + exp[i + 3:]
            i = 0
        elif (opr == '-'):
            exp[i] = opd1 - opd2
            exp = exp[:i + 1] + exp[i + 3:]
            i = 0
        else:
            i += 2
    return "{:.2f}".format(exp[0])
