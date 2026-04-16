from itertools import product
k, m = map(int, input().split())
lists = []
for _ in range(k):
    row = list(map(int, input().split()))
    lists.append([x**2 for x in row[1:]])
combinations = product(*lists)
max_value = 0
for combo in combinations:
    current_sum = sum(combo) % m
    if current_sum > max_value:
        max_value = current_sum
print(max_value)
