n = int(input())
arr = list(map(int, input().split(" ")))
a=[]
for i in arr:
    if(i not in a):
        a.append(arr.count(i))
for i in arr:
    if(arr.count(i)==max(a)):
        print(len(arr)-arr.count(i)) 
        break

    
