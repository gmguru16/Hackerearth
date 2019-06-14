def pairs(a, k):
    d = {}
    ans = 0
    for i in a:
        d[i] = i
    for j in a:
        g = j+k
        if g in d:
            ans +=1
    return ans
    
n,k=map(int,input().split())
a=list(map(int,input().split()))
print(pairs(a,k))
