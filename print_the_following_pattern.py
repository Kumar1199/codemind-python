n=int(input())
c=1
d=n-1
for i in range(1,n+1):
    for j in range(d):
        print(" ",end="")
    for k in range(c):
        print(i,end="")
    c+=2
    d-=1
    print()
    