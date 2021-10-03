s = set([i**5 for i in range(1, 150)])
p = 0.2
for a in s:
    for b in s:
        for c in s:
            for d in s:
                if a + b + c + d in s:
                    print(a**p+b**p+c**p+d**p+(a+b+c+d)**p)
                    exit()
