import sys

# recursion - brute force kind of technique
# BAD APPROACH
def solver1(arr, n):
    min_jumps = sys.maxsize

    def helper(i, jumps):
        nonlocal min_jumps
        if jumps > min_jumps:
            return
        if i == n - 1:
            min_jumps = min(min_jumps, jumps)
            return

        for j in range(arr[i]):
            if (i + j + 1) >= n:
                break
            helper(i + j + 1, jumps + 1)

    helper(0, 0)
    return -1 if (min_jumps == sys.maxsize) else min_jumps


# efficient approach
# greedy approach
def solver(arr, n):
    if arr[0] == 0:
        return -1
    if arr[0] >= n:
        return 1

    jumps = 1
    last_jump, last_index = arr[0], 0
    while last_jump != 0:
        if (last_index + last_jump >= n - 1):
            return jumps
        else:
            new_index, max_r, new_jump = 0, 0, 0
            # finding maximum jump possible in range from current index
            for _ in range(last_jump):
                last_index += 1
                if max_r <= last_index + arr[last_index]:
                    new_index = last_index
                    max_r = last_index + arr[last_index]
                    new_jump = arr[last_index]
            last_index = new_index
            last_jump = new_jump
        jumps += 1

    return -1
    


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solver(arr, n))
