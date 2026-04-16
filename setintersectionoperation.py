
n = input() 
english_subs = set(map(int, input().split()))
m = input() 
french_subs = set(map(int, input().split()))
common_subs = english_subs.intersection(french_subs)
print(len(common_subs))
