def gcd(n,m):
    if m==0:
        return n
    return gcd(m,n%m)
m,n=map(int,input().split())
print(gcd(m,n))