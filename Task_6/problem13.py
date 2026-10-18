# Set .union() Operation

# https://www.hackerrank.com/challenges/py-set-union/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n1=int(input())
setA=set(map(int,input().split()))
n2=int(input())
setB=set(map(int,input().split()))

print(len(setA.union(setB)))