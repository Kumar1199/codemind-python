n=int(input())
l=[int(x) for x in input().split()]
m=list(set(l))
c=0
k=0
for i in m:
    if l.count(i)>c:
        c=l.count(i)
        k=i
print(k)