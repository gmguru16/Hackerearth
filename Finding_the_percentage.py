n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
l=student_marks[query_name]
sum=0
for i in l:
    sum+=i
print('%.2f'%(sum/len(l)))


