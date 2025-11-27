f = open('17_17530.txt')
s = [int(x) for x in f]

m = min(s)

res = []

for i in range(len(s) - 1):
    a, b = s[i], s[i + 1]
    cond_1 = (a % 55 == m) + (b % 55 == m)
    if cond_1 > 0:
        res.append(a + b)


print(len(res), min(res))