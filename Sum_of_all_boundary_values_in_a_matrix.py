n,m=map(int,input().split())
mat=[]
for i in range(n):
    l=[int(x) for x in input().split()]
    mat.append(l)
c=0
for i in range(n):
    for j in range(m):
            if (i==0 or i==n-1) or (j==0 or j==m-1):
                c+=mat[i][j]
print(c)