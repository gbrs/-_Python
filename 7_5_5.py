n = int(input())
while n >= 10:
    last = n % 10
    n //= 10
print(last)
