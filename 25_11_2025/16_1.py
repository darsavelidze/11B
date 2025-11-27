import sys

sys.setrecursionlimit(1000000000)
sys.set_int_max_str_digits(10000000)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))