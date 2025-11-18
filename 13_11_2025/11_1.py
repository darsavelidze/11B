from math import ceil, floor

n = 3845627
Is = 11 * 2 ** 30
I = ceil(Is / n)

K = 2783

i = ceil(I * 8 / K)

N = 2 ** (i - 1) + 1

print(N)
