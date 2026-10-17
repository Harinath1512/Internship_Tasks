# Word Order

# https://www.hackerrank.com/challenges/word-order/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

N=int(input())
d={}
for i in range(N):
    a=input()
    if a in d:
        d[a]+=1
    else:
        d[a]=1
print(len(d.keys()))
for i in d.values():
    print(i,end=' ')
