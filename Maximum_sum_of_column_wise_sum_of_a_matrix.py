a,b=map(int,input().split())
mat=[]
for i in range(a):
    l=[int(x) for x in input().split()]
    mat.append(l)
n=[]
c=0
k=0
for i in range(max(a,b)):
    for j in range(a):
        for m in range(b):
            if m==k:
                c+=mat[j][m]
    n.append(c)
    k+=1
    c=0
print(max(n))