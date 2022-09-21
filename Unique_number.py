n=input()
n=[i for i in n]
s=[]
for i in n:
    if i not in s:
        s.append(i)
if n==s:
    print("Unique Number")
else:
    print("Not Unique Number")