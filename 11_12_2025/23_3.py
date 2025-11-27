def f(s, m):
    if s == m:
        return 1
    if s < m:
        return 0
    return f(s - 2, m) + f(s // 2, m)


print(f(38, 16) * f(16, 2))