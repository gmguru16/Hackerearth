t,i= int(input()),0
for i in range(t):
    m = int(input())
    n = int(input())
    arr = list(map(int, input().split(" ")))
    a,b=0,0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(arr[i]+arr[j]==m and a==0):
                a=i
                b=j
    print(str(a+1)+" "+str(b+1))
                
