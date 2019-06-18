st=input()
msg="SOS"
res=0
for i in range(len(st)):
    if(st[i]!=msg[i%3]):
        res+=1
print(res)
