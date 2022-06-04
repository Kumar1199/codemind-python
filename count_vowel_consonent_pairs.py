a=input()
b=a[::-1]
vowels="aeiouAEIOU"
count=0
c=0
for i in range(len(a)//2):
    if a[i] in vowels and b[i] not in vowels and b[i]!=" ":
        count=count+1
for i in range(len(a)//2):
    if a[i] not in vowels and b[i] in vowels and a[i]!=" ":
        count=count+1
print(count)