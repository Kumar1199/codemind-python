n=int(input())
k=[int(x) for x in input().split()]
f=1
for i in k:
    if i!=1 and i!=0:
        f=0
        break
if f==1:
    print(True)
else:
    print(False)