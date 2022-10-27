n=int(input())
k=n
c=1
while k:
    for i in range(c,n+1):
        print(i,end=" ")
    c+=1
    k-=1
    print()