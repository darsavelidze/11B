def divs(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return s


def get_primes(s):
    return [x for x in s if len(divs(x)) == 0 and str(x).count('5') == 1]

k = 0
for i in range(1_324_727, 10**10):
    divisors = divs(i)
    primes = get_primes(divisors)
    if len(primes) == 1 and primes[0] ** 2 == i:
        print(i, max(divisors))
        k += 1
    elif len(primes) == 2 and primes[0] * primes[1] == i:
        print(i, max(divisors))
        k += 1
    if k == 5:
        break
