# Symmetric Difference

# Enter your code here. Read input from STDIN. Print output to STDOUT
n1=int(input())
a1=input()
lis=a1.split()
newlis = list(map(int, lis))

n2=int(input())
a2=input()
lis2=a2.split()
newlis2 = list(map(int, lis2))

newlis=set(newlis)
newlis2=set(newlis2)

res=newlis.symmetric_difference(newlis2)
res=list(res)
res=sorted(res)
for i in res:
    print(i)