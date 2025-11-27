def f(s, m):
    if s == m:
        return 1
    if s > m or s == 11:
        return 0
    k = f(s + 1, m) + f(s * 2, m)
    if s != 1:
        k += f(s ** 2, m)
    return k


print(f(1, 20))