n=int(input())
l=[int(x) for x in input().split()]
m=int(input())
k=[int(x) for x in input().split()]
s=[]
for i in range(n):
    s.insert(k[i],l[i])
print(*s)