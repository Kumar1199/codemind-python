n=input().lower()
l=[]
for i in n:
    if i!=" " and n.count(i)==1:
        l.append(i)
print(len(l))