a=input()
vo="aeiouAEIOU"
di="0987654321"
v=0
c=0
s=0
d=0
for i in a:
    if i in vo:
        v+=1
    elif i in di:
        d+=1
    elif i==" ":
        s+=1
    else:
        c+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",s)
        