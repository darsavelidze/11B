from time import time
start = time()
s = set()
m = 'Hello how are you' * 10000000
for x in m:
    s.add(x)
print(time() - start)

start = time()
s = set(m)
print(time() - start)
