s,t=input(),input()
x=len(s)+len(t)
res=0
for i in s:
    if(i in t):
        a,b=s.count(i),t.count(i)
        if(a<b):
            res+=a
        else:
            res+=b
    s=s.replace(i,"")
    t=t.replace(i,"")
print(x-res*2)
