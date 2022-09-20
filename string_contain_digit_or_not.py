a=input()
b="0987654321"
c=0
for i in a:
    if i in b:
        c+=1
if c>0:
    print("Contains",c,"digit")
else:
    print("Doesn't contain digit")