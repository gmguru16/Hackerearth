n=int(input())
ii=1
while(ii<=n):
    s=input()
    str=s[0]
    for i in range(1,len(s)):
        if(str[len(str)-1]!=s[i]):
            str+=s[i]
    print(len(s)-len(str))
    ii+=1
            
        
