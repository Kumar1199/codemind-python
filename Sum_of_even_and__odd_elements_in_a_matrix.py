r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
even=0
odd=0
for i in range(r):
    for j in range(c):
        if mat[i][j]%2==0:
            even+=mat[i][j]
        else:
            odd+=mat[i][j]
print(even,odd)
        