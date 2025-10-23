f = open('9_23193.csv')

for line in f:
    s = [int(x) for x in line.split(',')]
    counts = [s.count(x) for x in s]
    cond_1 = counts.count(3) == 3 and counts.count(1) == 3
    povt = [x for x in s if s.count(x) > 1]
    ne_povt = [x for x in s if s.count(x) == 1]
    if cond_1:
        print(s, counts, povt, ne_povt)
