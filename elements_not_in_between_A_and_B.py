n=int(input())
l=[int(x) for x in input().split()]
a,b=map(int,input().split())
c=[]
for i in range(len(l)):
    if l[i]<a:
        c.append(l[i])
    elif l[i]>b:
        c.append(l[i])
if len(c)<1:
    print(-1)
else:
    print(*c)