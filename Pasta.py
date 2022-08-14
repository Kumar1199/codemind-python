a,b=map(int,input().split())
x=[int(x) for x in input().split()]
y=[int(y) for y in input().split()]
c=0
for i in y:
    if i in x:
        c+=1
        x.pop(x.index(i))
    else:
        break
if c==len(y):
    print("Yes")
else:
    print("No")