money = int(input())
coins = [1, 3, 4]
arr = [1000000000000000000000]*(money+1)
arr[0] = 0
for i in range(1, money+1):
    for coin in coins:
        if(i >= coin):
            temp = arr[i-coin]+1
            if(arr[i] > temp):
                arr[i] = temp
print(arr[money])
