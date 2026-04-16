def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    width = (size * 4) - 3
    lines = []
    for i in range(size):
        s = "-".join(alphabet[size-1:i:-1] + alphabet[i:size])
        lines.append(s.center(width, "-"))
    print('\n'.join(lines[::-1] + lines[1:]))

