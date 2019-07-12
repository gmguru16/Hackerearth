n = int(input())
c = set(input())
for i in range(n-1):
    a = set(input())
    c = c.intersection(a)
print(len(c))
