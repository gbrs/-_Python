mx = 150 ** 5
for a in range(1, 151):
    sma = a ** 5
    for b in range(a, int((mx - sma) ** 0.2) + 1):
        # print(b)
        smb = sma + b ** 5
        for c in range(b, int((mx - smb) ** 0.2) + 1):
            # print(c)
            smc = smb + c ** 5
            for d in range(c, int((mx - smc) ** 0.2) + 1):
                # print(d)
                smd = smc + d ** 5
                for e in range(int(smd ** 0.2) - 2, int(smd ** 0.2) + 2):
                    # print(e)
                    if smd == e ** 5:
                        print(a, b, c, d, e)
