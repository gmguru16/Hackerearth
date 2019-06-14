def triplets(a, b, c):
    a,b,c=list(sorted(set(a))),list(sorted(set(b))),list(sorted(set(c)))
    
    x,y,z,ans=0,0,0,0
    
    while (y < len(b)):
        while (x < len(a) and a[x] <= b[y]):
            x += 1
        
        while (z < len(c) and c[z] <= b[y]):
            z += 1
        
        ans += x * z
        y += 1
    
    return ans
    
n=list(map(int,input().split()))
a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=list(map(int, input().split()))
print(triplets(a,b,c))
