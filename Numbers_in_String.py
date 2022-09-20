a=input()
c=0
d="0987654321"
for i in a:
    if i in d:
        c+=int(i)
print(c)