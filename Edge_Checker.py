a,b=map(int,input().split())
c=[1,2,3,4,5,6,7,8,9,10,1]
if abs(b-a)==1:
    print("Yes")
elif (a==10 and b==1) or (b==10 and a==1):
    print("Yes")
else:
    print("No")
    