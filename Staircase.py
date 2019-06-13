n,i=int(input()),1
while(i<=n):
    s=""
    for j in range(i):
        s+="#"
    while(len(s)!=n):
        s=" "+s
    print(s)
    i+=1
