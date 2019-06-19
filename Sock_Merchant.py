n = int(input())
ar = list(map(int, input().split(" ")))
l=[]
res=0
for i in ar:
    if (i not in l):
        l.append(i)
for i in l:
    res+=(ar.count(i))//2
print(res)

    
