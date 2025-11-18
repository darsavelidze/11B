from itertools import product
def f(ip):
    return '.'.join([bin(x)[2:].zfill(8) for x in map(int, ip.split('.'))])

print(f('112.160.0.0'))
print(f('255.240.0.0'))

k = 0
for x in product('01', repeat=20):
    ip = '011100001010' + ''.join(x)
    if ip.count('1') % 5 == 0:
        k += 1
print(k)