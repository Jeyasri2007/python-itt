import re

for _ in range(int(input())):
    s = input()
    if (s.isalnum() and 
        len(s) == 10 and 
        len(set(s)) == 10 and 
        len(re.findall(r'[A-Z]', s)) >= 2 and 
        len(re.findall(r'[0-9]', s)) >= 3):
        print("Valid")
    else:
        print("Invalid")
