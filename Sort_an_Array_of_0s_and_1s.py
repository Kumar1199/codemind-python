n=int(input())
l=[int(i) for i in input().split()]
c=l.count(1)
for i in range(n-c):
    print(0,end=" ")
for i in range(c):
    print(1,end=" ")