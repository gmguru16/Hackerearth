s=input().lower()
alpha="abcdefghijklmnopqrstuvwxyz"
c=0
for i in alpha:
    x=s.count(i)
    if(x==0):
        c=1
        break
if(c==1):
    print("not pangram")
else:
    print("pangram")
