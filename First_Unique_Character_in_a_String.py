s=input()
c=-1
for i in s:
    if s.count(i)==1:
        c=s.index(i)
        break
print(c)