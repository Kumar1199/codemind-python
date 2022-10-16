n=int(input())
m=int(input())
mat=0
for i in range(n):
    l=[int(i) for i in input().split()]
    mat+=sum(l)
print(mat)