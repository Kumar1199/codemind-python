n=int(input())
l=[int(x) for x in input().split()]
print(*l[:n//2-1:-1],end=' ')
print(*l[:n//2])