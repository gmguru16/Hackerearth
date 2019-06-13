'''
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
'''

n=int(input())
a =list(map(int,input().split())) 
b=[]
pos,neg,zero=0,0,0
for i in a:
    if(i>0):
        pos+=1
    elif(i<0):
        neg+=1
    else:
        zero+=1
b.append(round(pos/n,6))
b.append(round(neg/n,6))
b.append(round(zero/n,6))

for i in b:
    x=str(i)
    if((len(x) - x.index('.') - 1)!=6):
        for i in range(0,6-(len(x) - x.index('.') - 1)):
            x+="0"
    print(x)
            
