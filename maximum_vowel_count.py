s=input().lower().split()
l=0
c="aeiou"
for i in s:
    s=0
    for j in i:
        if j in c:
            s+=1
    l=max(l,s)
print(l)