n,m=map(int,input().split())
mat=[]
for i in range(n):
    l=[int(x) for x in input().split()]
    mat.append(l)
c=0
for i in range(n):
    for j in range(m):
        if i==j or i+j==n-1:
            c+=mat[i][j]
print(c)