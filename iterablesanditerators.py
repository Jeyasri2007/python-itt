from itertools import combinations
# 1. Read Input
n = int(input())
letters = input().split()
k = int(input())
total_combos = list(combinations(range(n), k))
a_indices = [i for i, char in enumerate(letters) if char == 'a']
favorable_count = 0
for combo in total_combos:
    if any(idx in a_indices for idx in combo):
        favorable_count += 1
print(f"{favorable_count / len(total_combos):.4f}")
