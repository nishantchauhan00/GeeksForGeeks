# find longest increasing subsequence from both sides for every index
# then for every index sum both and decrease -1 as the current element
# is counted in both sequence(left right)
# print the maximum

def solver(arr, n):
    if n <= 1:
        return n

    # O(n^3)
    # left longest increasing subsequence
    left_lic = [1]*n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] and left_lic[i] < left_lic[j] + 1:
                left_lic[i] = left_lic[j] + 1
        
    # O(n^3)
    # right longest increasing subsequence
    right_lic = [1]*n
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if arr[i] > arr[j] and right_lic[i] < right_lic[j] + 1:
                right_lic[i] = right_lic[j] + 1
    
    # print(left_lic, right_lic)

    # O(n)
    longest_bitonic_subsequnce = 0
    for i in range(n):
        ith_bitonic_seq_len = abs(left_lic[i] + right_lic[i] - 1)
        if ith_bitonic_seq_len > longest_bitonic_subsequnce:
            longest_bitonic_subsequnce = ith_bitonic_seq_len

    return longest_bitonic_subsequnce









if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solver(arr, n))