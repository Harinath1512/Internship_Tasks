# Check Subset

# https://www.hackerrank.com/challenges/py-check-subset/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
for i in range(n):
    n1=int(input())
    setA=set(map(int,input().split()))
    n2=int(input())
    setB=set(map(int,input().split()))

    a=setA.intersection(setB)
    if a==setA:
        print('True')
    else:
        print('False')