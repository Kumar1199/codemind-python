from math import *
def prime(n):
    s=int(sqrt(n))+1
    if n==1:return False
    for i in range(2,s):
        if n%i==0:
            return False
    return True
def palin(n):
    if int(str(n)[::-1])==n:
        return True
    else:
        return False
def nexpp(n):
    while prime(n)==False or palin(n)==False:
        n=n+1
    return n
n=int(input())
print(nexpp(n+1))