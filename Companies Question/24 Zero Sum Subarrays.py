#code
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
from collections import Counter

def solver(arr, n):
    sum_total = 0
    count = [None]*n
    zerosumcount = 0
    count = Counter()

    for i in range(n):
        sum_total += arr[i]
        if sum_total is 0:
            zerosumcount += 1
        if count.get(sum_total):
            zerosumcount += count[sum_total]
        count[sum_total] += 1
    
    return zerosumcount



T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solver(arr, n))


