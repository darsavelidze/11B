from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 20:
        return n
    return (n - 6) * f(n - 1) + f(n - 1)

for i in range(1, 1000):
    f(i)

print(f(900))