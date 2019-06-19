i,j,k =map(int,input().split(" "))
res=0
for x in range(i,j+1):
    y=str(x)
    if((x-int(y[::-1]))%k==0):
        res+=1
print(res)
