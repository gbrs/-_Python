lst = []
for i in range(int(input()[1:])):
    lst.append(input())
for s in lst:
    if '#' in s:
        s = s[:s.find('#')].replace('#', '')
    print(s.rstrip())
