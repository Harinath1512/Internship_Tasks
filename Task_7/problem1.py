# Set .symmetric_difference() Operation

# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n1=int(input())
setA=set(map(int,input().split()))

n2=int(input())
setB=set(map(int,input().split()))

print(len(setA.symmetric_difference(setB)))