a=input()
c=0
for i in a:
    if i=="L":
        c-=1
    elif i=="R":
        c+=1
    elif i=="U":
        c+=1
    elif i=="D":
        c-=1
if c==0:
    print("True")
else:
    print("False")