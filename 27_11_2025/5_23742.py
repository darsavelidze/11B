import string


def f(x, base):
    alf = '0123456789' + string.ascii_uppercase
    res = ''
    while x > 0:
        res = alf[x % base] + res
        x //= base
    return res
