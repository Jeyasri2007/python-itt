import re

t = int(input())

for _ in range(t):
    s = input()
    pattern = r'^[+-]?[0-9]*\.[0-9]+$'
    if re.match(pattern, s):
        try:
            float(s)
            print(True)
        except:
            print(False)
    else:
        print(False)
