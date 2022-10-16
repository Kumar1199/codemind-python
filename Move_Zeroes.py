n=int(input())
l=[int(x) for x in input().split()]
c=0
for i in range(n):
    if l[i]==0:
        c+=1
for i in l:
    if i==0:
        l[l.index(i)]="`"
for i in range(c):
    l.append(0)
k=[]
for i in l:
    if i!="`":
        k.append(i)
print(*k)