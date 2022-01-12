from collections import deque


def backtrack(arr, n, w):
    final_ans = arr[n][w]
    bool_arr = [0 for j in range(w+1)]
    i = final_ans
    j = n
    while(i >= 0 and j >= 0):
        ans = arr[j][i]
        a = arr[j-1][i-weights[j]]+weights[j]
        b = arr[j-1][i]
        if(a > b):
            bool_arr[i-weights[j]] = 1
            i = i-weights[j]
        else:
            bool_arr[i] = 1
        j = j-1
    backtrack_list = []
    for i in range(w+1):
        if(bool_arr[i] != 0):
            backtrack_list.append(i)
    return backtrack_list


w, n = map(int, input().split())
weights = list(map(int, input().split()))
weights = deque(weights)
weights.appendleft(0)
weights = list(weights)
arr = [[0 for i in range(w+1)]for j in range(n+1)]
for j in range(1, n+1):
    for i in range(1, w+1):
        arr[j][i] = arr[j-1][i]
        if(weights[j] <= i):
            val = arr[j-1][i-weights[j]]+weights[j]
            if(val > arr[j][i]):
                arr[j][i] = val
print(arr[n][w])
#print(backtrack(arr, n, w))


#       0 1 2 3 4 5 6 7 8 9 10
#     0 0 0 0 0 0 0 0 0 0 0 0
# (1) 1 0
# (4) 2 0
# (8) 3 0
