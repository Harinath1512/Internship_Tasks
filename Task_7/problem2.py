# The Captain's Room

# https://www.hackerrank.com/challenges/py-the-captains-room/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i,j in d.items():
    if j==1:
        print(i)