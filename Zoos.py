s=input()
z=0
o=0
for i in s:
    if i=="z":
        z+=1
    if i=="o":
        o+=1
if o==z*2:
    print("Yes")
else:
    print("No")