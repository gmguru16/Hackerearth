t = int(input())
for t_itr in range(t):
    n,k = map(int,input().split(" "))
    a = list(map(int, input().split(" ")))
    res=0
    for i in a:
        if(i<=0):
            res+=1
    if(res>=k):
        print("NO")
    else:
        print("YES")
