f = open('9_3215.csv')
k = 0
for line in f:
    numbers = [int(i) for i in line.split(',')]
    s = sorted(numbers)
    if (s[0] + s[-1]) ** 2 > s[1] ** 2 + s[2] ** 2 + s[3] ** 2:
        k += 1
print(k)

