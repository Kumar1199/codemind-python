for i in range(int(input())):
    a=input()
    f=0
    c="0987654321"
    for i in a:
        if i in c:
            f=1
            break
    if f==1:
        print("Yes")
    else:
        print("No")