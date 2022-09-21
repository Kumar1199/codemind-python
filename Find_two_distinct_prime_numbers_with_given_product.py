n=int(input())
s=0
def prime(n):
    if n==1:return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        if prime(i)==True:
            if prime(n//i)==True:
                print(i,n//i)
                s=1
                break
if s==0:print(-1)