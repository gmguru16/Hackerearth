'''
There is a collection of input strings and a collection of query strings. 
For each query string, determine how many times it occurs in the list of input strings.
'''

string,i,j=int(input()),0,0
s,q=[],[]
while(i<string):
    s.append(input())
    i+=1
query=int(input())
while(j<query):
    q.append(input())
    j+=1

for i in q:
    print(s.count(i))
