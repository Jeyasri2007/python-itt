if __name__ == '__main__':
    n = int(raw_input())
    # raw_input() is used in Python 2 instead of input()
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print hash(t)