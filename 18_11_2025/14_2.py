import string

alf = '0123456789' + string.ascii_uppercase

for x in alf[:29]:
    a = int('923' + x + '874', 29)
    b = int('524' + x + '6152', 29)
    c = a + b
    if c % 28 == 0:
        print(c // 28)

# 10716

for x in range(1, 150):
    r = 5 * 150 ** 4 + 1 * 150 ** 3 + x * 150 ** 2 + 2 * 150 + 9 + x * 150 ** 3 + 2 * 150 + 3
    if r % 149 == 0:
        print(r // 149)

# 8418
for p in range(7, 10):
    for x in range(1, p):
        for y in range(1, p):
            for z in range(p):
                if y * p ** 2 + 4 * p + y + y * p ** 2 + 6 * p + 5 == x * p ** 3 + z * p ** 2 + 3 * p + 3:
                    print(int(str(x) + str(y) + str(z), p))


# 23198
for x in range(1, 3000):
    r = 9 ** 150 + 9 ** 30 - x
    k = 0
    while r > 0:
        if r % 9 == 0:
            k += 1
        r //= 9
    if k == 122:
        print(x)
        break