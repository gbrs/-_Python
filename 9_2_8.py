s = input()
middle = (len(s) - 1) // 2 + 1
print(s[middle:] + s[:middle])
