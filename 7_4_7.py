payment = int(input())
quantity = 0

for coin in (25, 10, 5, 1):
    quantity += payment // coin
    payment %= coin

print(quantity)
