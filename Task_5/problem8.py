# Set .add()

# https://www.hackerrank.com/challenges/py-set-add/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT

N=int(input())
a=[]
for i in range(N):
    val=input()
    a.append(val)
b=set(a)
print(len(b))
