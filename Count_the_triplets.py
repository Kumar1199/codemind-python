for i in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if (l[i]+l[j]) in l:
                c+=1
    if c==0:
        print(-1)
    else:
        print(c)