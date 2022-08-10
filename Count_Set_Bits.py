for i in range(int(input())):
    n=int(input())
    b=bin(n)
    l=[i for i in str(b)]
    print(l.count("1"))