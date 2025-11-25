f = open('17_23563.txt')

s = [int(x) for x in f]

m_p_35 = min([x for x in s if x > 0 and x % 35 == 0])

m = []

for i in range(len(s) - 1):
    a, b = s[i], s[i + 1]
    if a != b and abs(a - b) % m_p_35 == 0:
        m.append(a + b)

print(len(m), max(m))
