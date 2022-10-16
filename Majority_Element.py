n=int(input())
l=[int(x) for x in input().split()]
c=0
v=0
for i in range(n):
    if l.count(l[i])>c:
        c=l.count(l[i])
        v=l[i]
print(v)