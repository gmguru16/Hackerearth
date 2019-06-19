q = int(input())
for i in range(q):
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    x1,y1=abs(x-z),abs(y-z)
    if(x1<y1):
        print("Cat A")
    elif(y1<x1):
        print("Cat B")
    else:
        print("Mouse C")
