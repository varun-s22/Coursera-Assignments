

# def binary_search(array, key):
#     # write your code here
#     low = 0
#     high = len(array)-1
#     found_index = -1
#     while(low <= high):
#         mid = (low+high)//2
#         if(array[mid] == key):
#             found_index = mid
#             break
#         elif(array[mid] > key):
#             high = mid-1
#         else:
#             low = mid+1
#     return found_index


# def GetRightPosition(A, l, r, key):
#     while(r - l > 1):
#         m = l + (r - l)//2

#         if(A[m] <= key):
#             l = m
#         else:
#             r = m
#     return l


# def GetLeftPosition(A, l, r, key):
#     while(r - l > 1):
#         m = l + (r - l)//2

#         if(A[m] >= key):
#             r = m
#         else:
#             l = m
#     return r


# def CountOccurances(A, size, key):
#     left = GetLeftPosition(A, -1, size-1, key)
#     right = GetRightPosition(A, 0, size, key)

#     if(key == A[left] and key == A[right]):
#         return right-left+1
#     else:
#         return 0


# ans_storer = []
# if __name__ == '__main__':
#     num_keys = int(input())
#     input_keys = list(map(int, input().split()))
#     assert len(input_keys) == num_keys

#     num_queries = int(input())
#     input_queries = list(map(int, input().split()))
#     assert len(input_queries) == num_queries

#     for key in input_queries:
#         count = CountOccurances(input_keys, num_keys, key)
#         if(count != 0):
#             index = binary_search(input_keys, key)-count+1
#         else:
#             index = binary_search(input_keys, key)
#         ans_storer.append(index)
#     for index in ans_storer:
#         print(index, end=" ")
#     print("\n")
n = int(input())
seq = list(map(int, input().split()))
k = int(input())
keys = list(map(int, input().split()))
d = {}
for i in range(n):
    if seq[i] in d:
        pass
    else:
        d[seq[i]] = i
ans = []
for key in keys:
    if key in d:
        ans.append(d[key])
    else:
        ans.append(-1)
for ele in ans:
    print(ele, end=" ")
print("\n")
