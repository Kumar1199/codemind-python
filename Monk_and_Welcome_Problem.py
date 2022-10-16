n=int(input())
a=[int(a) for a in input().split()]
b=[int(b) for b in input().split()]
for i in range(n):
    print(a[i]+b[i],end=" ")