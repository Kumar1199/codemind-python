n,m=map(int,input().split())
l=[int(x) for x in input().split()]
s=0
d=0
for i in l:
    if s<2:
        if i>m:
            s+=1
        else:
            d+=1
print(d)