from itertools import product
def f(ip):
    return '.'.join([bin(x)[2:].zfill(8) for x in map(int, ip.split('.'))])

k = 0
for tail in product('01', repeat=4):
    s = f('192.168.32.160')[:-4]
    s += ''.join(tail)
    if s.count('1') % 2 == 0:
        k += 1

print(k)