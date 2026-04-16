a = set(input().split())
n = int(input())
is_strict_superset = True

for _ in range(n):
    other = set(input().split())

    if not (a > other):
        is_strict_superset = False
        break

print(is_strict_superset)
