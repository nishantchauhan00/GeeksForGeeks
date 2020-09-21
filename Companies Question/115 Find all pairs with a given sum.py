'''
# brute force, although it is not giving tle, but still slow
# 1.43s
def solver(arr1, n1, arr2, n2, k):
    arr1.sort()
    arr2.sort()
    out = []
    for i in range(n1): 
        for j in range(n2): 
            if arr1[i] + arr2[j] == k:
                out.append([arr1[i], arr2[j]])
            elif arr1[i] + arr2[j] > k:
                break
    return out


T = int(input())
for _ in range(T):
    n1, n2, k = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    out = solver(arr1, n1, arr2, n2, k)
    if len(out) > 0:
        print(", ".join("{0} {1}".format(el[0], el[1]) for el in out))
    else:
        print("-1")
'''

'''
Constraints:
1 <= T <= 100
1 <= N, M, X <= 10^6
-10^6 <= A, B <= 10^6

So, x or k is always positive
'''
# more efficient O(n) solution, 0.59s
def solver(arr1, n1, arr2, n2, k):
    out = []
    for i in range(n1):
        if (k - arr1[i]) in arr2:
            out.append([arr1[i], k-arr1[i]])
    return out


T = int(input())
for _ in range(T):
    n1, n2, k = map(int, input().split())
    arr1 = list(map(int, input().split()))
    # # instead of sorting input array, just sort the smaller output array
    # arr1.sort() 
    arr2 = set(list(map(int, input().split())))

    out = solver(arr1, n1, arr2, n2, k)
    if len(out) > 0:
        out.sort()
        print(", ".join("{0} {1}".format(el[0], el[1]) for el in out))
    else:
        print("-1")