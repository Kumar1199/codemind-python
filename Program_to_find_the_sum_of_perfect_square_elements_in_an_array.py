n=int(input())
l=[int(x) for x in input().split()]
c=0
for i in l:
    if i**0.5==int(i**0.5):
        c+=i
print(c)