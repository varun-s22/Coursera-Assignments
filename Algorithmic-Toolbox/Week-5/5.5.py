def lcs(X, Y, Z, l, m, n):

    arr = [[[0 for i in range(n+1)] for j in range(m+1)]
           for k in range(l+1)]
    for i in range(l+1):
        for j in range(m+1):
            for k in range(n+1):
                if (i == 0 or j == 0 or k == 0):
                    arr[i][j][k] = 0

                elif (X[i-1] == Y[j-1] and
                      X[i-1] == Z[k-1]):
                    arr[i][j][k] = arr[i-1][j-1][k-1] + 1

                else:
                    arr[i][j][k] = max(max(arr[i-1][j][k],
                                           arr[i][j-1][k]),
                                       arr[i][j][k-1])
    return arr[l][m][n]


n = int(input())
X = list(map(int, input().split()))

m = int(input())
Y = list(map(int, input().split()))

l = int(input())
Z = list(map(int, input().split()))

print(lcs(X, Y, Z, n, m, l))
