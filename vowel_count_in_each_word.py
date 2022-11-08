a=input().lower()
b=a.split()
c="aeiou"
for i in b:
    s=0
    for j in i:
        if j in c:
            s+=1
    print(s,end=" ")