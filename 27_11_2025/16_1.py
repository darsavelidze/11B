cache = [-1] * 100000


def g(n):
    if cache[n] != -1:
        return cache[n]
    if n < 10:
        return 2 * n
    return g(n - 2) + 1


def f(n):
    return 2 * (g(n - 3) + 8)

for i in range(1, 15500):
    cache[i] = g(i)

print(f(15548))