def f(s1, s2, m):
    if s1 + s2 >= 79:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s1 + 1, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1 + s2, s2, m - 1), f(s1, s1 + s2, m - 1)]
    if m % 2 != 0:
        return any(h)
    return all(h)


print([x for x in range(1, 70) if f(9, x, 2)])
print([x for x in range(1, 70) if not f(9, x, 1) and f(9, x, 3)])
print([x for x in range(1, 70) if not f(9, x, 2) and f(9, x, 4)])
