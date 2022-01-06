def partition(arr, i, j):
    pivot = (j+i)//2
    while(j > i):
        if(arr[i] > arr[pivot] and arr[j] < arr[pivot]):
            arr[i], arr[j] = arr[j], arr[i]
            i = i+1
            j = j-1
        elif(arr[i] > arr[pivot] and arr[j] >= arr[pivot]):
            j = j-1
        elif(arr[i] <= arr[pivot] and arr[j] < arr[pivot]):
            i = i+1
        else:
            i = i+1
            j = j-1
    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j


def quicksort(arr, i, j):
    if(j > i):
        end = partition(arr, i, j)
        quicksort(arr, i, end-1)
        quicksort(arr, end+1, j)


n = int(input())
arr = list(map(int, input().split()))
new_arr = sorted(arr)
for j in new_arr:
    print(j, end=" ")
print("\n")
