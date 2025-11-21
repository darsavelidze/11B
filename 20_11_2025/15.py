# 23274

for A in range(1, 50):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            F = ((2 * x + y) != 110) or (x < y) or (A < x)
            if F == 0:
                flag = False
    if flag:
        print(A)

# # 17556
for A in range(1, 1000):
    flag = True
    for B in range(70, 91):
        for x in range(1, 100):
            F = (x % A == 0) or ((x == B) <= (x % 22 != 0))
            if F == 0:
                flag = False
    if flag:
        print(A)


# # 17556
B = range(70, 91)
for A in range(1, 1000):
    flag = True
    for x in range(1, 100):
        F = (x % A == 0) or ((x in B) <= (x % 22 != 0))
        if F == 0:
            flag = False
    if flag:
        print(A)


# 4279

for A in range(1, 1000):
    flag = True
    for x in range(1, 10000):
        F = (x & 1097 == 0) <= ((x & 2047 != 0) <= (x &A != 0))
        if F == 0:
            flag = False
    if flag:
        print(A)
