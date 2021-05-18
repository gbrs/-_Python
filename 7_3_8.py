'''1−2+3−4+5−6+…+(−1)^n+1 * n'''

n = int(input())
s = 0
for i in range(1, n + 1):
    s += i * (-1)**(i % 2 + 1)

print(s)
