n,m=map(int,input().split())
mat=[]
for i in range(n):
    l=[int(x) for x in input().split()]
    mat.append(l)
c=0
for i in mat:
    if i==sorted(i) or i[::-1]==sorted(i):
        c+=1
print(c)