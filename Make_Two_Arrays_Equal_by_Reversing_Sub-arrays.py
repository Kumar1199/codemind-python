n=int(input())
l=[int(i) for i in input().split()]
m=int(input())
k=[int(x) for x in input().split()]
if sorted(l)==sorted(k):
    print(True)
else:
    print(False)