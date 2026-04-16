
_ = input()  
a = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    cmd_name = input().split()[0]
    other_set = set(map(int, input().split()))
    getattr(a, cmd_name)(other_set)
print(sum(a))
