a=int(input())
b=[int(x) for x in input().split()]
c,d=map(int,input().split())
e=[]
for i in range(len(b)):
    if b[i]<c:
        e.append(b[i])
for i in range(len(b)):
    if b[i]>d:
        e.append(b[i])
if len(e)>0:
    print(max(e))
else:
    print(-1)