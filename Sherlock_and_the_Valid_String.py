s=input()
s=''.join(sorted(s))
res=0
l,j=[],{}
for i in s:
    res=s.count(i)
    if(res!=0):
        l.append(res)
        j[i]=res
    s=s.replace(i,"")

if((l.count(l[0]))==len(j)-1) or ((l.count(l[0]))==len(j)):
    print("YES")
else:
    print("NO")

