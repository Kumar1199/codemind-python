n=int(input())
l=[int(x) for x in input().split()]
c=0
d=0
for i in range(n):
    if i%2!=0:
        c+=l[i]
    else:
        d+=l[i]
if abs(c-d)%4==0:
    print("X")
else:
    print("Y")