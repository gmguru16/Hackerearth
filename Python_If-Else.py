n=int(input())
if(n%2!=0):
    print("Weird")
elif(n%2==0):
    if(n>=6 and n<=20):
        print("Weird")
    elif(n>20 or (n>=2 and n<=5)):
        print("Not Weird")
