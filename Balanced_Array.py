for i in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    c=0
    for i in range(n):
        if sum(l[:i])==sum(l[i+1:]):
            c=1
            break
    if c==1:
        print("YES")
    else:
        print("NO")