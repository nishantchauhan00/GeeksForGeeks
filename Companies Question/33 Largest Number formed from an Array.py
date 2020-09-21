# code
from functools import cmp_to_key


def compare(x, y):
    if int(x + y) > int(y + x):
        return 1
    elif int(x + y) < int(y + x):
        return -1
    else:
        return 0


def solver(arr, n):
    arr = sorted(arr, key=cmp_to_key(compare), reverse=True)
    return arr


T = int(input())

for _ in range(T):
    n = input()
    arr = input().split()
    print("".join(solver(arr, int(n))))
