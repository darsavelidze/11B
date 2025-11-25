def od(n, m):
    for i in range(2, min(n, m) - 1):
        if n % i == 0 and m % i == 0:
            return True
    return False