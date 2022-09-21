a,b=map(int,input().split())
c=str(a)[:b]
d=str(a)[::-1]
e=d[:b]
f=e[::-1]
print(abs(int(c)-int(f)))