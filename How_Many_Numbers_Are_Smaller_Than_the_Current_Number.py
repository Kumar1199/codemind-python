n=int(input())
l=[int(x) for x in input().split()]
for i in l:
    c=0
    for j in l:
        if j<i:
            c+=1
    print(c,end=" ")