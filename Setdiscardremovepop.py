import sys

def solve():
    try:
        input_data = sys.stdin.read().split()
        if not input_data:
            return
       
        n = int(input_data[0])
        s = set(map(int, input_data[1:n+1]))
        m = int(input_data[n+1])
       
        idx = n + 2
        for _ in range(m):
            if idx >= len(input_data):
                break
            cmd = input_data[idx]
            idx += 1
           
            if cmd == "pop":
                if s:
                    s.pop()
            elif cmd == "remove":
                val = int(input_data[idx])
                idx += 1
                if val in s:
                    s.remove(val)
            elif cmd == "discard":
                val = int(input_data[idx])
                idx += 1
                s.discard(val)
       
        print(sum(s))
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
