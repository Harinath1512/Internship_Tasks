# Set Mutations

# https://www.hackerrank.com/challenges/py-set-mutations/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
sup=set(map(int,input().split()))
N=int(input())

for i in range(N):
    a=input().split()
    s=set(map(int,input().split()))
    if a[0]=='intersection_update':
        sup.intersection_update(s)
    elif a[0]=='symmetric_difference_update':
        sup.symmetric_difference_update(s)
    elif a[0]=='difference_update':
        sup.difference_update(s)
    elif a[0]=='update':
        sup.update(s)
print(sum(sup))