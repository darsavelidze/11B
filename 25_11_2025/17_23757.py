f = open('17_23757 (1).txt')

s = [int(x) for x in f]
min_2 = min([x for x in s if 10 <= x <= 99])
m = []

for i in range(len(s) - 1):
    a, b = s[i], s[i + 1]
    cond_1 = (10 <= a <= 99) + (10 <= b <= 99)
    if cond_1 == 1 and (a + b) % min_2 == 0:
        m.append(a + b)

print(len(m), max(m))
