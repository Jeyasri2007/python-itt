from itertools import combinations_with_replacement
s, k = input().split()
k = int(k)
sorted_s = sorted(s)
result = combinations_with_replacement(sorted_s, k)
for combo in result:
    print("".join(combo))
