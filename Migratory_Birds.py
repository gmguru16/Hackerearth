n=int(input())
a=list(map(int,input().split(" ")))
x,y=[],[]
z=0

for i in a:
    if i not in x:
        x.append(i)
        z=max(z,a.count(i))    

for i in x:
    if(z==a.count(i)):
        y.append(i)
y=sorted(y)
print(y[0])
