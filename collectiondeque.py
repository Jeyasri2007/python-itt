
from collections import deque

d = deque()
n = int(input())
for _ in range(n):
    input_data = input().split()
    command = input_data[0]
    if len(input_data) > 1:
        value = input_data[1]
        getattr(d, command)(value)
    else:
        getattr(d, command)()
print(*(d))
