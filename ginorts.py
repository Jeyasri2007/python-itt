def sort_key(char):
    if char.islower():
        return (0, char) 
    elif char.isupper():
        return (1, char) 
    elif char.isdigit():
        val = int(char)
        if val % 2 != 0:
            return (2, char) 
        else:
            return (3, char)
s = input().strip()
sorted_s = sorted(s, key=sort_key)
print("".join(sorted_s))
