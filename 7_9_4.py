def count_divisors(number):
    cnt = 1
    for divisor in range(2, number + 1):
        if number % divisor == 0:
            cnt += 1
    return cnt


for number in range(1, int(input()) + 1):
    print(number, '+' * count_divisors(number), sep='')
