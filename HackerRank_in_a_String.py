n=int(input())
while(n>0):
    s=input()
    s1="hackerrank"
    if(len(s)<len(s1)):
        print("NO")
    else:
        j=0
        for i in range(0,len(s)):
            if(j<len(s1) and s[i]==s1[j]): 
                    j+=1
        if(j==len(s1)):
            print("YES")
        else:
            print("NO")
    n-=1
