n=int(input())
b=bin(n)
c=[i for i in str(b)]
c.pop(1)
c.pop(0)
d=[]
for i in c:
    if i=="1":
        d.append(0)
    else:
        d.append(1)
a=1
ans=0
for i in range(len(d)-1,0,-1):
    if d[i]==1:
        ans+=d[i]*a
        a*=2
    else:
        a*=2
print(ans)