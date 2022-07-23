r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
sum=0
for i in range(r):
    for j in range(c):
        sum+=mat[i][j]
print(sum)
        