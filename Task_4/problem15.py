# Word Order

N=int(input())
d={}
for i in range(N):
    a=input()
    if a in d:
        d[a]+=1
    else:
        d[a]=1
print(len(d.keys()))
for i in d.values():
    print(i,end=' ')
