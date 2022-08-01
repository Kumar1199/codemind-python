def hn(n):
    a=0
    while n>0:
        r=n%10
        a=a+r**2
        n=n//10
    return a
n=int(input())
while n>7:
    n=hn(n)
if n==1:
    print(True)
else:
    print(False)

        
