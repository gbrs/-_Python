n = int(input())
while n > 9:
    sm = 0
    n2 = n
    while n2 > 0:
        sm += n2 % 10
        n2 //= 10
    n = sm
print(n)
