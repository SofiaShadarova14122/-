x=float(input())
n=float(input())
f=1
k=0
if k==n:
    print(f)
elif k<n:
    while k<n:
        f*=x
        k+=1
    print (f)
else:
    n*=(-1)
    while k<n:
        f*=x
        k+=1
    print (1/f)
    
