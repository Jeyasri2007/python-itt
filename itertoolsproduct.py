from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = product(a, b)
print(*result)
