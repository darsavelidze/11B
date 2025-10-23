s = [1, 1, 1, 1, 2, 2, 2, 2]

s = [[s.count(x), x] for x in s]
print(s)
print(max(s))
