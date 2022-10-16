n=int(input())
l=[int(x) for x in input().split()]
for i in range(0,n,2):
    for j in range(l[i]):
        print(l[i+1],end=" ")