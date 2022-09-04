n=int(input())
mat1=[]
mat2=[]
for i in range(n):
    l=[int(x) for x in input().split()]
    mat1.append(l)
for i in range(n):
    l=[int(x) for x in input().split()]
    mat2.append(l)
mat=[]
for i in range(n):
    l=[]
    for j in range(n):
        l.append(abs(mat1[i][j]-mat2[i][j]))
    mat.append(l)
for i in mat:
    print(*i)
    