for i in range(int(input())):
    number=int(input())
    x=number
    octalnumbers=[0,1,10,11,100,101,110,111]
    output=[]
    while(x!=0):
        reminder=x%1000
        output.append(octalnumbers.index(reminder))
        x=x//1000
    output.reverse()
    o=[str(x) for x in output]
    print("".join(o))
