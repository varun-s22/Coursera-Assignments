def fibonaci(n):
    if(n<=1):
        return n
    a1=0
    a2=1
    i=2
    c=1
    while(i<=n):
        c=a1+a2
        a1=a2
        a2=c
        i=i+1
    return c
n=int(input())
print((fibonaci(n)*fibonaci(n+1))%10)
