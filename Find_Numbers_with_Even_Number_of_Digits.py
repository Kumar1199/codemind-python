n=int(input())
l=[i for i in input().split()]
c=0
for i in l:
    if len(i)%2==0:
        c+=1
print(c)