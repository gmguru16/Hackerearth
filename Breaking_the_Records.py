n=int(input())
l=list(map(int,input().split(" ")))
mini,maxi=[l[0]],[l[0]]
min,max=l[0],l[0]
for i in range(1,len(l)):
    if(min>l[i]):
        min=l[i]
    if(max<l[i]):
        max=l[i]
    if (min not in mini):
        mini.append(min)
    if (max not in maxi):
        maxi.append(max)
print(str(len(maxi)-1)+" "+str(len(mini)-1))

