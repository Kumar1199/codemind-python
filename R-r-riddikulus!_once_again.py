n,m=map(int,input().split())
l=[int(x) for x in input().split()]
for i in range(m%n):
    s=l.pop(0)
    l.append(s)
print(*l)