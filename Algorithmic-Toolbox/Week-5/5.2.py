n = int(input())
# x2 x3 +1
arr = [0]*(n+1)
for i in range(2, n+1):
    if(i == 2 or i == 3):
        arr[i] = 1
    else:
        if(i % 3 == 0):
            a = arr[i//3]+1
            b = arr[i-1]+1
            arr[i] = min(a, b)
        elif(i % 2 == 0):
            a = arr[(i//2)]+1
            b = arr[i-1]+1
            arr[i] = min(a, b)
        else:
            arr[i] = arr[i-1]+1
print(arr[n])


# Backtracking the numbers leading to n
nums = [n]
while n != 1:
    if n % 3 == 0 and arr[n]-1 == arr[n//3]:
        nums += [n//3]
        n = n//3
    elif n % 2 == 0 and arr[n]-1 == arr[n//2]:
        nums += [n//2]
        n = n//2
    else:
        nums += [n-1]
        n = n - 1

print(' '.join([str(i) for i in nums][::-1]))
