a=input()
b=a.split()
m=[]
for i in b:
    c=[k for k in i]
    l=[]
    for i in range(len(c)):
        if c[i].isalpha():
            l.append(c[i])
            c[i]="~"
    l.sort()
    for i in range(len(c)):
        s=0
        for j in l:
            if c[i]=="~" and s==0:
                c[i]=j
                l.pop(0)
    m.append(c)
for i in m:
    print("".join(i),end=" ")