a=int(input())
b=str(int(str(a)[::-1])**2)
if str(a**2)[::-1]==b:
    print(True)
else:
    print(False)