number = int(input())
answer = ''
while number > 0:
    answer = str(number % 2) + answer
    number //= 2
print(answer)
