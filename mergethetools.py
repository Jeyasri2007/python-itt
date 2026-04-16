def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        t_i = string[i:i + k]
        u_i = []
        for char in t_i:
            if char not in u_i:
                u_i.append(char)
        print("".join(u_i))

