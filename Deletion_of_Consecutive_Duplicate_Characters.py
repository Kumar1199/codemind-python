for i in range(int(input())):    
    n=input()
    a=[i for i in n]
    c=0
    for i in range(1,len(a)):
        if a[i]==a[i-1]:
            c+=1
    print(c)