n=int(input())
a=list(map(int,input().split(" ")))
d,m=map(int,input().split(" "))
ans=0
for i in range(len(a)):
    n=0
    count=0
    while(n<m):
        count+=a[i+n]
        n+=1
    if(count==d):
        ans+=1
    if(i+n==len(a)):
        break
print(ans)
