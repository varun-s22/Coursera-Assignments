def pisano(m):
    a1=0
    a2=1
    c=0
    for i in range(m**2):
        a1,a2=a2,(a1+a2)%m
        if(a2==1 and a1==0):
            c=i+1
            break
    return c
def fibonaci(n,m):
    a1=0
    a2=1
    if(n<=1):
        return n%m
    c=0
    i=2
    while(i<=n):
        c=a1+a2
        a1=a2
        a2=c
        i=i+1
    return c%m
n,m=map(int,input().split())
l=pisano(m)
remainder=n%l
print(fibonaci(remainder,m))
