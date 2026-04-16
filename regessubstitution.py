import re

def transform_symbols(line):
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)  
    return line
n = int(input())
for _ in range(n):
    print(transform_symbols(input()))
