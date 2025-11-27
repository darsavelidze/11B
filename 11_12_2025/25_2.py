def divs(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return s

k = 0
for i in range(800_000, 10**10):
    divisors = divs(i)
    if len(divisors) > 0:
        M = min(divisors) + max(divisors)
        if M % 10 == 4:
            k += 1
            print(i, M)

    if k == 5:
        break