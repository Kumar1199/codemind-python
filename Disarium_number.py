n=int(input())
b=int(str(n)[::-1])
s=0
i=1
while b>0:
    r=b%10
    s=s+r**i
    i+=1
    b=b//10
if s==n:
    print(True)
else:
    print(False)