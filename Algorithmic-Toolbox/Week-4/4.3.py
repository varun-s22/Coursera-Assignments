n = int(input())
arr = list(map(int, input().split()))
d = {}
for i in arr:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
c = max(list(d.values()))
if(c > (n//2)):
    print(1)
else:
    print(0)
