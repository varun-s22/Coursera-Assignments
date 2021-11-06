n = int(input())
d = {}
a = n
for i in range(1, n+1):
    if(a-i < 0):
        break
    if(a-i) in d.keys():
        continue
    else:
        d[i] = 1
        a = a-i
        if(a == 0):
            break
q = list(d.keys())
l = len(q)
if(a != 0):
    q[l-1] = q[l-1]+a
print(l)
if(l == 1):
    print(n)
else:
    for j in q:
        print(j, end=" ")
print("\n")
