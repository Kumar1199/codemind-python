n=input()
m=n.split()
c=0
d="AEIOUaeiou"
for i in m:
    o=0
    l=-1
    for j in range(len(i)//2):
        if i[j] in d and i[l] not in d or i[j] not in d and i[l] in d:
            o+=1
        l-=1
    c+=o
print(c)