a,b=map(int,input().split())
mat=[]
for i in range(a):
    l=[int(x) for x in input().split()]
    mat.append(l)
l=[]
c=0
k=0
for m in range(max(a,b)):
    for i in range(a):
        for j in range(b):
            if j==k:
                c+=mat[i][j]
    l.append(c)
    k+=1
    c=0
print(*l)