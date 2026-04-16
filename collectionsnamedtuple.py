from collections import namedtuple
n, Student = int(input()), namedtuple('Student', input().split())
marks = [int(Student(*input().split()).MARKS) for _ in range(n)]
print("{:.2f}".format(sum(marks) / n))
