def f(s, m):
    if s == m:
        return 1
    if s > m or s == 17:
        return 0
    return f(s + 1, m) + f(s * 2, m)


print(f(1, 10) * f(10, 35))