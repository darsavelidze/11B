s = open('24_66.txt').readline()

count = 0
m = float('-inf')
i = 0
while i < len(s) - 3:
    if s[i:i + 3] == 'KOT':
        count += 1
        i += 3
    else:
        m = max(count, m)
        count = 0
        i += 1

print(m)
