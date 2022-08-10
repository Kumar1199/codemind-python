for i in range(int(input())):
    n=[int(x) for x in input().split()]
    for i in n:
        if n.count(i)==1:
            print(i)