# 17867

from itertools import product

def f(ip):
    return '.'.join(bin(x)[2:].zfill(8) for x in map(int, ip.split('.')))

k = 0
for x in product('01', repeat=11):
    s = ''.join(x)
    if (8 + s.count('1')) % 5 != 0:
        k += 1

print(k)




print(bin(248)[2:])
print(bin(172)[2:], bin(16)[2:], bin(168)[2:])
k = 0
for i in range(2**11):
    if (8 + str(bin(i)[2:]).count('1')) % 5 != 0:
        k += 1
print(k)




