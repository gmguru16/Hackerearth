n,k = map(int,input().split(" "))
height = list(map(int, input().split(" ")))
b=max(height)-k
if(b<0):
    print(0)
else:
    print(b)

    
