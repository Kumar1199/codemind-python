n=int(input())
l=[int(x) for x in input().split()]
for i in range(0,len(l),2):
    for j in range(l[i+1]):
        print(l[i],end=" ")