n,k=map(int,input().split(" "))
a=list(map(int,input().split(" ")))
res=0
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):

        if((a[i]+a[j])%k==0):
            res+=1
print(res)
