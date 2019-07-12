n=int(input())
s=input()
k=int(input())
s1=""
for i in s:
    if(i.isupper()): 
        s1+=chr((ord(i)+k-65)%26+65) 
    elif(i.islower()): 
        s1+=chr((ord(i)+k-97)%26+97) 
    else:
        s1+=i
print(s1)
