import re

def solve():
    s = input()
    k = input()
   
    pattern = re.compile(r'(?=(' + re.escape(k) + r'))')
   
    matches = list(pattern.finditer(s))
   
    if not matches:
        print("(-1, -1)")
    else:
        for m in matches:
            start = m.start(1)
            end = m.end(1) - 1
            print("({0}, {1})".format(start, end))

if __name__ == "__main__":
    solve()
