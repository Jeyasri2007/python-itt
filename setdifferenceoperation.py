_ = input()
english_subs = set(map(int, input().split()))
_ = input()
french_subs = set(map(int, input().split()))

print(len(english_subs.difference(french_subs)))
