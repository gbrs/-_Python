texts = [input() for _ in range(int(input()))]
queries = [input() for _ in range(int(input()))]
for text in texts:
    if all(query.lower() in text.lower() for query in queries):
        print(text)
