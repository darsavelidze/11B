def f(ip):
    return '.'.join(bin(x)[2:].zfill(8) for x in map(int, ip.split('.')))

print(f('216.54.187.235'))
print(f('216.54.174.128'))