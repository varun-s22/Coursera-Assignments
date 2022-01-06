def binary_search(key, array):
    low = 0
    high = len(array)-1
    found_index = -1
    while(low <= high):
        mid = (low+high)//2
        if(array[mid] == key):
            found_index = mid
            break
        elif(array[mid] > key):
            high = mid-1
        else:
            low = mid+1
    return found_index


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
search_these_elements = list(map(int, input().split()))
index_array = []
for key in search_these_elements:
    index = binary_search(key, arr)
    index_array.append(index)
for j in index_array:
    print(j, end=" ")
print("\n")
