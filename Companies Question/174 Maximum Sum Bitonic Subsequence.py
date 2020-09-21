# find maximum sum increasing subsequence from both sides for every index
# then for every index sum both and decrease element as the current element
# is counted in both sequence(left right)
# print the maximum 

def solver(arr, n):
    if n <= 1:
        return sum(arr) # handles zero element too, so i used sum

    # O(n^3)
    # left longest increasing subsequence
    l_max_inc_seq = arr.copy()
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] and l_max_inc_seq[i] < l_max_inc_seq[j] + arr[i]:
                l_max_inc_seq[i] = l_max_inc_seq[j] + arr[i]
        
    # O(n^3)
    # right longest increasing subsequence
    r_max_inc_seq = arr.copy()
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if arr[i] > arr[j] and r_max_inc_seq[i] < r_max_inc_seq[j] + arr[i]:
                r_max_inc_seq[i] = r_max_inc_seq[j] + arr[i]
    
    # print(l_max_inc_seq, r_max_inc_seq)

    # O(n)
    maxsum_bitonic_subsequnce = 0
    for i in range(n):
        ith_bitonic_seq_len = abs(l_max_inc_seq[i] + r_max_inc_seq[i] - arr[i])
        if ith_bitonic_seq_len > maxsum_bitonic_subsequnce:
            maxsum_bitonic_subsequnce = ith_bitonic_seq_len

    return maxsum_bitonic_subsequnce









if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solver(arr, n))