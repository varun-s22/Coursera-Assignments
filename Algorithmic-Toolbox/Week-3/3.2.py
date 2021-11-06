n, W = map(int, input().split())
arr = []
for i in range(n):
    v, w = map(int, input().split())
    arr.append([v/w, w])
a = sorted(arr, reverse=True)
left_weight = W
sum2 = 0
for j in range(n):
    weight = min(a[j][1], left_weight)
    sum2 = sum2+weight*a[j][0]
    left_weight = left_weight-weight
print(f"{sum2:.4f}")
