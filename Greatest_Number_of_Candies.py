n=int(input())
l=[int(x) for x in input().split()]
k=int(input())
s=max(l)
for i in l:
    if i+k>=s:
        print(True,end=" ")
    else:
        print(False,end=" ")