a=input()
c=[]
e="aeiouAEIOU"
d=[i for i in a]
for i in range(len(d)):
    if d[i] in e:
        c.append(d[i])
        d[i]="~"
for i in range(len(d)):
    if d[i]=="~":
        s=c.pop()
        d[i]=s
print("".join(d))