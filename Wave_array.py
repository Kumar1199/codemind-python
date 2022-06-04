a=int(input())
b=[int(x) for x in input().split()]
count=0
f = 1
for i in range(0,len(b)-2, 2):
    if b[i]<b[i+1]:
        if b[i+1]>b[i+2]:
            count = count+1
        else:
            f = 0
            break
    elif b[i]>b[i+1]:
        if b[i+1]<b[i+2]:
            count = count+1
        else:
            f = 0
            break
print("yes") if f == 1 else print("no")