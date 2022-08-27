def palin(n):
    if int(str(n)[::-1])==n:return True
    return False
def pp(n):
    n=n-1
    while palin(n)==False:
        n=n-1
    return n
def np(n):
    n=n+1
    while palin(n)==False:
        n=n+1
    return n
n=int(input())
if n-pp(n)<np(n)-n:
    print(pp(n))
elif np(n)-n<n-pp(n):
    print(np(n))
else:
    print(pp(n),np(n))