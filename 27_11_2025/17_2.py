f = open('17_16383.txt')
s = [int(x) for x in f]

m_21 = [x for x in s if abs(x) % 100 == 21 and len(str(abs(x))) == 5]

res = []

for i in range(1, len(s)):
    a, b = s[i - 1], s[i]
    cond_1 = (a in m_21) + (b in m_21)
    cond_2 = a * a + b * b >= max(m_21) ** 2
    if (cond_1 == 1) and cond_2:
        res.append(a + b)

print(len(res), max(res))
