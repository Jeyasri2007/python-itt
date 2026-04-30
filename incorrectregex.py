import re

def solve():
    try:
        t_str = raw_input()
        if not t_str:
            return
        t = int(t_str)
        for _ in range(t):
            s = raw_input()
            try:
                re.compile(s)
                print True
            except re.error:
                print False
    except EOFError:
        pass

if __name__ == "__main__":
    solve()