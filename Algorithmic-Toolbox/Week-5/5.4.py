# longest common subsequence via dp
n = int(input())
seq1 = list(map(int, input().split()))
m = int(input())
seq2 = list(map(int, input().split()))
arr = [[-1 for i in range(n+1)]for j in range(m+1)]
for i in range(n+1):
    arr[0][i] = 0
for j in range(m+1):
    arr[j][0] = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        if(seq1[j-1] == seq2[i-1]):
            arr[i][j] = arr[i-1][j-1]+1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
print(arr[m][n])
