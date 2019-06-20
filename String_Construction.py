q = int(input())
for q_itr in range(q):
    s = input()
    l=[]
    for i in s:
        if(i not in l):
            l.append(i)
    print(len(l))
