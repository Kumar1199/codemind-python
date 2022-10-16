n=int(input())
l=[int(x) for x in input().split()]
k=[0]*n
for i in range(n):
    if l.index(max(l))==i:
        l[i]=0
    k[i]=max(l)
    l[i]=0
    s=l.index(max(l))
k[-1]=-1
print(*k)