s1=input().lower()
s2=input().lower()
a = {i for i in s1 if i.isalpha()}
b = {i for i in s2 if i.isalpha()}
s=a.intersection(b)
x = list(s)
# x.remove(' ')
# l=[]
# for i in s:
#     if i!=" " and s.count(i)>1:
#         l.append(i)
# k=[]
# for i in l:
#     if i not in k:
#         k.append(i)
if len(x)>0:
    print("".join(sorted(x)))
else:
    print(-1)

