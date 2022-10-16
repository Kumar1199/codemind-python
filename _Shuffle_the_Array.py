n=int(input())
l=[int(c) for c in input().split()]
a=l[:n//2]
b=l[n//2:]
for i in range(n//2):
    print(a[i],b[i],end=" ")