from itertools import groupby
s = input().strip()
results = []
for k, g in groupby(s):
    count = len(list(g))
    results.append(f"({count}, {k})")
print(" ".join(results))
