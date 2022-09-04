a=input().lower()
b=input().lower()
f=1
for i in a:
    if i not in b:
        f=0
        break
if f==1:print(True)
else:print(False)