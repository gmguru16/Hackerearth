n,i=int(input()),0

while(i<n):
    x=int(input())
    
    if(x>=38):
        y=((x//5)+1)*5
        if(y-x<3):
            x=y
    print(x)
    i+=1
    
            #https://www.hackerrank.com/challenges/grading/problem
