n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l1.sort(reverse=True)
l2.sort(reverse=True)
sum2 = 0
for j in range(n):
    sum2 = sum2+l1[j]*l2[j]
print(sum2)
