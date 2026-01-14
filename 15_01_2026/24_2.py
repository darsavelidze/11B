from collections import deque

f = open('24_18186.txt').readline()
s = 'BCDFGH'
vowels = 'AE'
pair = deque(maxlen=2)

max_len = float('-inf')

for i in range(len(f) - 2):
    if f[i] in s and f[i + 1] in s and f[i + 2] in vowels:
        pair.append(i)
        if len(pair) == 2:
            max_len = max(pair[-1] - pair[-2] + 3, max_len)

print(max_len)
