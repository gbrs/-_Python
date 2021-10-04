s = input()
mx = 0
for char in s:
    cnt = s.count(char)
    if cnt >= mx:
        mx_char = char
        mx = cnt
print(mx_char)
