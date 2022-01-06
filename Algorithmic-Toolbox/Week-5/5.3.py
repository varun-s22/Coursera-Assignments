s1 = input()
s2 = input()
l2 = len(s1)
l1 = len(s2)
arr = [[-1 for i in range(l1+1)]for j in range(l2+1)]
arr[0][0] = 0
for i in range(1, l1+1):
    arr[0][i] = i
for j in range(1, l2+1):
    arr[j][0] = j
for i in range(1, l1+1):
    for j in range(1, l2+1):
        a = arr[j-1][i]+1
        b = arr[j][i-1]+1
        c = arr[j-1][i-1]+1
        if(s2[i-1] == s1[j-1]):
            arr[j][i] = min(a, b, c-1)
        else:
            arr[j][i] = min(a, b, c)
print(arr[l2][l1])

#       d i s t a n c e
#     0 1 2 3 4 5 6 7 8
# e   1 1
# d   2
# i   3
# t   4
# i   5
# n   6
# g   7
