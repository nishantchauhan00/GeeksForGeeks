'''
arr[] = {1, 4, -2, -2, 5, -4, 3}

If we consider all prefix sums, we can
notice that there is a subarray with 0
sum when :
1) Either a prefix sum repeats or
2) Or prefix sum becomes 0.

Prefix sums for above array are:
1, 5, 3, 1, 6, 2, 5

Since prefix sum 1 repeats, we have a subarray
with 0 sum. 
'''
def solver(arr, n):
    sum_total = 0
    count = [None]*n
    for i in range(n):
        sum_total += arr[i]
        if sum_total in count or sum_total == 0:
            return True
        count[i] = sum_total
    # print(count)
    return False



T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print("Yes" if solver(arr, n) else "No")


