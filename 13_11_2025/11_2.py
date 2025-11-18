data = [[(0, "R", 1), (0, "R", 1), (1, "R", 1)],
        [(1, "R", 2), (1, "R", 2), (2, "R", 2)],
        [(3, "R", 0), (3, "R", 0), (3, "S", 0)]]

s = ['l'] + ['0', '1'] * 500 + ['l']

action = data[0][-1]
i = 1
while True:
    if s[i] == 'l':
        break
    s[i] = action[0]
    action = data[action[2]][i]

print(s)
