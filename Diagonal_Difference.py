n=int(input())
matrix=[]
for i in range(n):     
    a =list(map(int,input().split())) 
    matrix.append(a)
fir,sec=0,0
for i in range(n):
    fir+=matrix[i][i]
    sec+=matrix[i][(n-1)-i]
print(abs(fir-sec)
