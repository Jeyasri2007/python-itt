
n = input()
english_subs = set(map(int, input().split()))
m = input()
french_subs = set(map(int, input().split()))
total_subs = english_subs.union(french_subs)
print(len(total_subs))
