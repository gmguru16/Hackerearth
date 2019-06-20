i = input()
 
s = []

for c in i:
    if (c not in  s):
        s.append(c)
    else:
        if (s[-1] == c):
            s.pop()
        else:
            s.append(c)
             
if (len(s)==0):
    print ("Empty String")
else:
    print (''.join(s))
