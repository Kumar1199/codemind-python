for i in range(int(input())):
    a,b=map(int,input().split())
    c=0
    for i in range(a,b+1):
        if str(i)[len(str(i))-1:]=="2" or str(i)[len(str(i))-1:]=="3" or str(i)[len(str(i))-1:]=="9":
            c+=1
    print(c)