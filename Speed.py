for i in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    c=1
    for i in range(1,n):
        if l[i]<=l[i-1]:
            c+=1
    print(c)