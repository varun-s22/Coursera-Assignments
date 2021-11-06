d = int(input())
m = int(input())
n = int(input())
stop_list = list(map(int, input().split()))
stoplist2 = []
stoplist2.append(0)
for k in stop_list:
    stoplist2.append(k)
stoplist2.append(d)
num_refills = 0
curr = 0
while(curr <= n):
    last = curr
    while(curr <= n and stoplist2[curr+1]-stoplist2[last] <= m):
        curr += 1
    if(last == curr):
        num_refills = -1
        break
    if(curr <= n):
        num_refills += 1
print(num_refills)
