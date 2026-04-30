n, x = map(int, input().split())
marks = [map(float, input().split()) for _ in range(x)]

for student_marks in zip(*marks):
    print(sum(student_marks) / x)
