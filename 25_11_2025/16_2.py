cache= [-1] * 10000

def f(n):
    if cache[n] != -1:
        return cache[n]
    if n < 20:
        return n
    return (n - 6) * f(n - 1) + f(n - 1)

for i in range(1, 1000):
    cache[i] = f(i)

print(f(900))
