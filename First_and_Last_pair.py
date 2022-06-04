a=int(input())
b=[int(x) for x in input().split()]
c=b[::-1]
d=[]
for i in range(len(c)//2):
    d.append(c[i])
if len(c)%2!=0:
    d.append(0)
for i in range(len(d)):
    print(b[i],d[i],end=" ")