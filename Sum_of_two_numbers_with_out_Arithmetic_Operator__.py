x,y=map(int,input().split())
while y!=0:
    d=x&y
    x=x^y
    y=d<<1
print(x)