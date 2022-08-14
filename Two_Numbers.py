n=int(input())
a=[int(x) for x in input().split()]
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
b.sort()
print(*b)