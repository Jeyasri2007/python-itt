from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

for i in range(1, n + 1):
    word = input().strip()
    d[word].append(i)
for _ in range(m):
    word_b = input().strip()
    if word_b in d:
        print(*(d[word_b]))
    else:
        print("-1")
