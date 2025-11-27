P = {2, 4, 8, 12, 15}
W = {3, 6, 8, 15}


for A in range(1, 100):
    flag = True
    for x in range(1, 20):
        F = (x in P) <= ((x not in W) or (x == A))
        if F == 0:
            flag = False
    if flag:
        print(A)

print(A)
