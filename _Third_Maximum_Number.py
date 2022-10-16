n=int(input())
l=[int(x) for x in input().split()]
l=list(set(l))
if len(l)>2:
    l.pop(l.index(max(l)))
    l.pop(l.index(max(l)))
print(max(l))