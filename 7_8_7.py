for b in range(100 // 10 + 1):
    for k in range(100 // 5 + 1):
        for t in range(101):
            if b + k + t == 100 and 10 * b + 5 * k + 0.5 * t == 100:
                print(b, k, t)
