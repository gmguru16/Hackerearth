n,k=map(int,input().split())
a=list(map(int,input().split()))

mod = k % n 
s = "" 

for i in range(n): 
    print (str(a[(mod + i) % n]),end=" ") 
    




