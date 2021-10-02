"""28n+30k+31m=365"""
for n in range(365 // 28 + 1):
    for k in range(365 // 30 + 1):
        for m in range(365 // 31 + 1):
            if 28 * n + 30 * k + 31 * m == 365:
                print(n, k, m)
