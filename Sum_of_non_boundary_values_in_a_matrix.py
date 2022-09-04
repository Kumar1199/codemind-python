n,m=map(int,input().split())
mat=[]
for i in range(n):
    l=[int(x) for x in input().split()]
    mat.append(l)
c=0
for i in range(1,n-1):
    for j in range(1,m-1):
            c+=mat[i][j]
print(c)