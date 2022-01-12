string = input()
symbol = []
number = []
for i in range(len(string)):
    if(i % 2 == 0):
        number.append(int(string[i]))
    else:
        symbol.append(string[i])

max_arr = [[0 for i in range(len(number))]for j in range(len(number))]
min_arr = [[0 for i in range(len(number))]for j in range(len(number))]

for j in range(len(number)):
    max_arr[j][j] = number[j]
    min_arr[j][j] = number[j]


def get_max(i, j):
    temp_max = -1000000000000000000000000
    temp_min = 1000000000000000000000000
    for k in range(i, j):
        if(symbol[k] == "+"):
            a = max_arr[i][k]+max_arr[k+1][j]
            b = max_arr[i][k]+min_arr[k+1][j]
            c = min_arr[i][k]+min_arr[k+1][j]
            d = min_arr[i][k]+max_arr[k+1][j]
        elif(symbol[k] == "-"):
            a = max_arr[i][k]-max_arr[k+1][j]
            b = max_arr[i][k]-min_arr[k+1][j]
            c = min_arr[i][k]-min_arr[k+1][j]
            d = min_arr[i][k]-max_arr[k+1][j]
        elif(symbol[k] == "*"):
            a = max_arr[i][k]*max_arr[k+1][j]
            b = max_arr[i][k]*min_arr[k+1][j]
            c = min_arr[i][k]*min_arr[k+1][j]
            d = min_arr[i][k]*max_arr[k+1][j]
        temp_max = max(a, b, c, d, temp_max)
        temp_min = min(a, b, c, d, temp_min)
    return temp_max, temp_min


m = len(number)
for x in range(1, m):
    for i in range(m-x):
        j = i+x
        max_arr[i][j], min_arr[i][j] = get_max(i, j)

print(max_arr[0][m-1])
