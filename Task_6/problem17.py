# Check Strict Superset

# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

sup=set(map(int,input().split()))
n=int(input())
res=True
for i in range(n):
    s=set(map(int,input().split()))
    if not sup.issuperset(s) or sup==s:
        res=False
        break
print(res)