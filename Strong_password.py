numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
n=int(input())
s=input()
res=0
if any(i in numbers for i in s )==False:
    res+=1
if any(i in lower_case for i in s )==False:
    res+=1
if any(i in upper_case for i in s )==False:
    res+=1
if any(i in special_characters for i in s )==False:
    res+=1
print(max(res,6-len(s)))
