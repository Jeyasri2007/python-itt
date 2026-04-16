import re
n, m = map(int, input().split())
matrix = [input() for _ in range(n)]
decoded_string = "".join([matrix[row][col] for col in range(m) for row in range(n)])
final_output = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', decoded_string)
print(final_output)
