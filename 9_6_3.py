n = int(input())
s = input()
decode = ''
for char in s:
    if ord(char) - ord('a') >= n:
        decode += chr(ord(char) - n)
    else:
        decode += chr(ord('z') - (n - (ord(char) - ord('a'))) + 1)
print(decode)
