n=input()
l=[i for i in n]
c=0
for i in range(len(l)):
    if l.count(l[i])==1:
        print(l[i])
        c=1
        break
if c==0:
    print(-1)