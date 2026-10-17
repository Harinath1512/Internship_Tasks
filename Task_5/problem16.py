# Collections.Counter()

# https://www.hackerrank.com/challenges/collections-counter/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
X=int(input())
y=input()
sizes=list(map(int,y.split()))
N=int(input())
cash=0
for i in range(N):
    size,price=map(int,input().split())
    if size in sizes:
        cash+=price
        sizes.remove(size)
print(cash)
