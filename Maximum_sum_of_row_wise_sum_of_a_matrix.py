a,b=map(int,input().split())
mat=[]
for i in range(a):
    l=[int(x) for x in input().split()]
    mat.append(l)
l=[]
for i in mat:
    l.append(sum(i))
print(max(l))