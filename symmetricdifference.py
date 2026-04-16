
m = input() 
a = set(map(int, input().split()))
n = input() 
b = set(map(int, input().split()))
diff = a.symmetric_difference(b)
for val in sorted(diff):
    print(val)
