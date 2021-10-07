'''def make_divisors_list(number):
    lst = [1]
    for divisor in range(2, number + 1):
        if number % divisor == 0:
            lst.append(divisor)
    return lst


print(make_divisors_list(int(input())))'''



n = int(input())
print([divisor for divisor in range(1, n + 1) if not n % divisor])
