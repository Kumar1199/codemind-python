n=int(input())
l=[int(x) for x in input().split()]
k=int(input())
if k in l:
    print(l.index(k))
else:
    print(-1)