import re

n = int(input())
in_bracket = False

for _ in range(n):
    line = input()
    if '{' in line:
        in_bracket = True
    if '}' in line:
        in_bracket = False
    if in_bracket:
        matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', line)
        for match in matches:
            print(match)
