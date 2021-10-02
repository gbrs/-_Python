n = int(input())
for i in range(1, n + 1):
    for j in range(i if i <= n // 2 else n - i + 1):
        print('*', end='')
    print()
