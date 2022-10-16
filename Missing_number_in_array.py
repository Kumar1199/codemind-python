for i in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    print(n*(n+1)//2-sum(l))