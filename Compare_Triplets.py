l=[int(i) for i in input().split()]
m=[int(i) for i in input().split()]
lc=0
mc=0
for i in range(len(l)):
    if l[i]>m[i]:
        lc+=1
    elif m[i]>l[i]:
        mc+=1
print(lc,mc)