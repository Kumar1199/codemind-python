n=int(input())
d=[]
c=1
for i in range(1,n+1):
    d.append(c)
    c*=2
if n in d:
    print(True)
else:
    print(False)
    