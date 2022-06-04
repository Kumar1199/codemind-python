a=int(input())
b=[int(x) for x in input().split()]
c,d=map(int,input().split())
e=0
for i in range(len(b)):
    if b[i]<c:
        e=e+b[i]
for i in range(len(b)):
    if b[i]>d:
        e=e+b[i]
print(e)