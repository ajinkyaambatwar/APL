n=1
nold=1
print(1,str(nold))
print(2,str(n))
k=3
while k<11:
    new=n+nold
    nold=n
    n=new
    print(k, new)
    k=k+1
