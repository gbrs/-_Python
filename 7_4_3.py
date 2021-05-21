word = input()

cnt = 0
while word != 'стоп' and word != 'хватит' and word != 'достаточно':
    cnt += 1
    word = input()

print(cnt)
