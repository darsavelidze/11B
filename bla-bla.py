def f(s, m):
    if s >= 43:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s +1, m - 2), f(s * 2, m - 1), f(s * 3, m - 1)]
    if m % 2 != 0:
        return any(h)
    else:
        return all(h)
print([x for x in range(1, 43) if f(x, 2)])
print([x for x in range(1, 43) if not f(x, 1) and f(x, 3)])
print([x for x in range(1, 43) if not f(x, 2) and f(x, 4)])