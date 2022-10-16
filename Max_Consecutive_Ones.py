n=int(input())
l=[int(x) for x in input().split()]
c=0
k=0
for i in l:
    if i==1:
        k+=1
    else:
        c=max(c,k)
        k=0
c=max(c,k)
print(c)