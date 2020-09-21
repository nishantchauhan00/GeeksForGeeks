# brute force - loop through whole array with each cycle and rot the tomatoes.
# At last check if there is any left tomato
# BAD WAY
def solver1(arr, r, c):
    changed = True
    rotten_val, time = 2, 0
    # if there was no change in previous cycle then break
    while changed:
        changed = False
        for i in range(r):
            for j in range(c):
                # if tomato is not rotten, check if can be rotten
                if arr[i][j] == 1:
                    # check for rotten tomatoes in four directions
                    if (
                        (i - 1 != -1 and arr[i - 1][j] == rotten_val)
                        or (i + 1 != r and arr[i + 1][j] == rotten_val)
                        or (j - 1 != -1 and arr[i][j - 1] == rotten_val)
                        or (j + 1 != c and arr[i][j + 1] == rotten_val)
                    ):
                        arr[i][j] = rotten_val * 2
                        changed = True

        time += 1  # timer
        rotten_val *= 2

    # check if any tomato is left unrotten, print -1, else time-1
    return -1 if any(1 in row for row in arr) else time - 1


# GOOD WAY
from collections import deque
# using bfs
def solver(arr, r, c):
    time = 1
    qu = deque(maxlen=r * c)

    # push all 2's or rotten tomatoes to queue
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 2:
                qu.append([i, j, time])

    # start bfs
    while qu:
        i, j, time = qu.popleft()

        # check for rotten tomatoes in four directions
        # rot it if unrotten and put it in queue
        if i - 1 != -1 and arr[i - 1][j] == 1: # top
            arr[i - 1][j] = 2
            qu.append([i - 1, j, time + 1])

        if i + 1 != r and arr[i + 1][j] == 1: # bottom
            arr[i + 1][j] = 2
            qu.append([i + 1, j, time + 1])

        if j - 1 != -1 and arr[i][j - 1] == 1: # left
            arr[i][j - 1] = 2
            qu.append([i, j - 1, time + 1])

        if j + 1 != c and arr[i][j + 1] == 1: # right
            arr[i][j + 1] = 2
            qu.append([i, j + 1, time + 1])

    return -1 if any(1 in row for row in arr) else time - 1


T = int(input())
for i in range(T):
    r, c = map(int, input().split())
    arr = [[None for _ in range(c)] for _ in range(r)]
    temparr = list(map(int, input().split()))
    for i in range(r):
        for j in range(c):
            arr[i][j] = temparr[i * c + j]

    print(solver(arr, r, c))
