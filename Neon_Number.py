n=int(input())
b=n**2
s=0
while b>0:
    r=b%10
    s=s+r
    b=b//10
if n==s:
    print("Neon Number")
else:
    print("Not Neon Number")