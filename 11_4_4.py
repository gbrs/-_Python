lst = [input() for _ in range(int(input()))]
st = set()
for s in lst:
    if s not in st:
        print(s)
        st.add(s)
