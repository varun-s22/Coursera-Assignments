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
n=int(input())
a1=0
a2=1
i=2
c=1
l=pisano(10)
nn=n%l
while(i<=nn+2):
    c=a1+a2
    a1=a2
    a2=c
    i=i+1
print((c-1)%10)
