def maxLen1(arr, N): # brute force
    out = 0
    zero, one = 0, 0
    for i in range(n):
        for j in range(i, n):
            if arr[j] == 0:
                zero += 1
            else:
                one += 1
            if zero == one:
                out = max(out, zero+one)
        zero, one = 0, 0
    return out


# just an optimization: we can skip making 0s to -1
# and just consider 0s as -1 while solving question by using if condition
def maxLen(arr, N):
    # convert 0s to -1, then find out maximum length
    # of subarray with sum 0
    for i in range(N):
        if arr[i] == 0:
            arr[i] = -1
    
    hmap = {}
    max_len, curr_sum = 0, 0
    for i in range(N):
        curr_sum += arr[i]
        
        if curr_sum == 0:
            max_len = i + 1
        
        # >if: curr_sum already occured, that means zero sum occurred
        #  at (current position - last position at which it occurs)
        # >else:if not occured then make a new entry
        if curr_sum in hmap:
            # we dont need to update in hmap because if the value strikes
            # third time then we will take from first reference not second
            max_len = max(max_len, i - hmap[curr_sum])
        else:
           hmap[curr_sum] = i
            
    return max_len
    


T = int(input())
for _ in range(T):
    n = int(input())
    arr = map(int, input().split())
    print(maxLen(arr, n))

