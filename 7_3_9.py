max1 = max2 = 0
for _ in range(int(input())):
    number = int(input())
    if number > max1:
        max2, max1 = max1, number
    elif number > max2:
        max2 = number

print(max1, max2, sep='\n')
