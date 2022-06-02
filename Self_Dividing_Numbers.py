def self(n):
    f=1
    for d in str(n):
        if d=="0" or n%int(d)>0:
            f=0
    return f
a=int(input())
b=int(input())
for i in range(a,b+1):
    if self(i)==1:
        print(i,end=" ")