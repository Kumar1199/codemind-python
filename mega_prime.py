def prime(n):
    if n==1:return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return False
    return True
n=int(input())
def p(n):
    c=0
    while n>0:
        r=n%10
        if prime(r)==False:
            c=1
            break
        n=n//10
    if c==0:return True
    return False
if prime(n)==True and p(n)==True:
    print("Mega Prime")
else:
    print("Not Mega Prime")