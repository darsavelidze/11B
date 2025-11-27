s = open('24_10105.txt').readline()
print(len(s))
s = s.split('T')
m = []
for i in range(len(s)- 100):
    line = s[i:i + 100]
    su = sum([len(x) for x in line])
    m.append(su + 100)
    if i % 100000 == 0:
        print(i)