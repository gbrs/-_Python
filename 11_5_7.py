pair_counter = [0, 0]
cnt = 0
sm = 0

# создаю список из количеств пар, которые можно создать с i элементами
for i in range(1, 99):
    cnt += i
    pair_counter.append(cnt)

lst = list(map(int, input().split()))

# перебираю все встречающиеся в списке числа и считаю сколько раз каждое встречается
# и добавляю в сумматор количество пар, которые могут создать одинаковые числа
for number in set(lst):
    sm += pair_counter[lst.count(number)]
print(sm)
