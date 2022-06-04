a=int(input())
b=[int(x) for x in input().split()]
f=1
for i in range(len(b)-1):
    if b[i]>=b[i+1]:
        f=0
if f==1:
    print("yes")
else:
    print("no")