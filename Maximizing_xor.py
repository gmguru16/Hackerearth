m,n=int(input()),int(input())
l=[]
for i in range(m,n+1):
    for j in range(i,n+1):
        l.append(i^j)
print(max(l))Maximizing XOR

