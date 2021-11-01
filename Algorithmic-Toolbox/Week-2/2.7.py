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
def find_fn(nn):
    a1=0
    a2=1
    i=2
    c=1
    while(i<=nn+2):
        c=a1+a2
        a1=a2
        a2=c
        i=i+1
    return (c-1)
m,n=map(int,input().split())
l=pisano(10)
nn=n%l
mm=m%l
print((find_fn(nn)-find_fn(mm-1))%10)
