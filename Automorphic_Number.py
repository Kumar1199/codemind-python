n=int(input())
s=str(n**2)
if s.endswith(str(n)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")