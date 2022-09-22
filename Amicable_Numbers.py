n=int(input())
m=int(input())
l=[i for i in range(1,n) if n%i==0]
k=[i for i in range(1,m) if m%i==0]
if sum(l)==m and sum(k)==n:
    print("Amicable")
else:
    print("Not Amicable")