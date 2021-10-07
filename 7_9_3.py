def count_divisors(number):
    cnt = 1
    sum_divisors = 1
    for divisor in range(2, number + 1):
        if number % divisor == 0:
            cnt += 1
            sum_divisors += divisor
    return cnt, sum_divisors


max_sum = 0
for number in range(int(input()), int(input()) + 1):
    current_counter, current_sum = count_divisors(number)
    if current_sum >= max_sum:
        max_divisors = current_counter
        max_number = number
        max_sum = current_sum

print(max_number, max_sum)
