for i in range(int(input())):
    c=1
    l=int(input())
    l=[int(i) for i in str(l)]
    l.sort()
    for i in range(1,len(l)):
        if l[i]-l[i-1]!=1:
            c=0
    if c==1:
        print("YES")
    else:
        print("NO")