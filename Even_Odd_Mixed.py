n=int(input())
l=[int(i) for i in str(n)]
e=1
ev=0
for i in l:
    if i%2==0:
        ev+=1
    else:
        e=0
if e==1:
    print("Even")
elif e==0 and ev==0:
    print("Odd")
else:
    print("Mixed")
