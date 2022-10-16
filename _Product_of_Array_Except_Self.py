n=int(input())
l=[int(x) for x in input().split()]
c=1
for i in range(len(l)):
    c*=l[i]
for i in range(n):
    print(c//l[i],end=" ")