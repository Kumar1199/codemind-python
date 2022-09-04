a=input()
b=a.split()
c=0
for i in b:
    if i.lower()==i[::-1].lower():
        c+=1
print(c)