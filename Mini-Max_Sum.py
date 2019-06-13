a=list(map(int,input().split()))
x,y=0,0
for i in a:
    x+=i
print(str(x-max(a))+" "+str(x-min(a)))
