grade = int(input())

cnt = 0
while -1 < grade < 6:
    if grade == 5:
        cnt += 1
    grade = int(input())

print(cnt)
