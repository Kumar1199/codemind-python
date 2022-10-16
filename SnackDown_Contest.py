for i in range(int(input())):
    n=int(input())
    p=[int(x) for x in input().split()]
    q=[int(x) for x in input().split()]
    a=p.pop(0)
    b=q.pop(0)
    c=list(set(p+q))
    if len(c)==n:
        print("YES")
    else:
        print("NO")