# No Idea!

# https://www.hackerrank.com/challenges/no-idea/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
lis=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))

happy=0

for i in lis:
    if i in A:
        happy+=1
    elif i in B:
        happy-=1
    else:
        happy=happy
print(happy)
