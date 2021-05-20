n = int(input())
a = 0
b = 1
print(b, end=' ')
for i in range(n - 1):
    print(a + b, end=' ')
    a, b = b, a + b
