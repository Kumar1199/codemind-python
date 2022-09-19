n=input()
s=0
for i in n:
    if i.isalpha()==False:
        s+=int(i)
print(s)