a=input()
b=a.split()
m=[]
for i in b:
    c=[i for i in i]
    l=[]
    k="aeiou"
    for i in range(len(c)):
        if c[i] not in k:
            l.append(c[i])
            c[i]="~"
    l.sort()
    for i in range(len(c)):
        s=0
        for j in l:
            if c[i]=="~" and s==0:
                c[i]=j
                l.pop(0)
                s=1
    m.append(c)
for i in m:
    print("".join(i),end=" ")