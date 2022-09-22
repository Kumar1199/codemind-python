def prime(n):
    if n==1:return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return False
    return True
def pp(n):
    while prime(n)==False:
        n-=1
    return n
def np(n):
    while prime(n)==False:
        n+=1
    return n
n=int(input())
x=pp(n)
y=np(n)
if n-x<=y-n:
    print(n-x)
else:
    print(y-n)