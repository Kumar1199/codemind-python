a,b=[int(x) for x in input().split()]
maximum=max(a,b)
p=maximum
while True:
    if p%a==0 and p%b==0:
        lcm=p
        break
    p=p+maximum
print(lcm)