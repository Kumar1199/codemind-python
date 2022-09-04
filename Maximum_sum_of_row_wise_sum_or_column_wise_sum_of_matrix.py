n,m=map(int,input().split())
mat=[]
for i in range(n):
    l=[int(x) for x in input().split()]
    mat.append(l)
k=[]
for i in mat:
    k.append(sum(i))
print(max(k))