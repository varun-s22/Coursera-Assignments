def find_num_of_digits(num):
    a = str(num)
    return len(a)


def find_largest_num_of_digits(arr):
    maxi = 0
    for i in range(len(arr)):
        if(find_num_of_digits(arr[i]) > maxi):
            maxi = find_num_of_digits(arr[i])
    return maxi


def iterateit(num, m):
    p = str(num)*(m+1)
    return p[:m+1]


n = int(input())
ele = list(map(int, input().split()))
m = find_largest_num_of_digits(ele)
new_arr = []
for i in range(n):
    st = iterateit(ele[i], m)
    new_arr.append([ele[i], st])
final_arr = sorted(new_arr, key=lambda x: x[1], reverse=True)
ans = ""
for i in final_arr:
    ans = ans+str(i[0])
print(ans)
