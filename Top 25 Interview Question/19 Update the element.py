"""
Replace every array element by multiplication of previous and next
"""


def update(arr):  # time: O(n)   space: O(n)
    carr = arr.copy()
    for i in range(1, len(arr) - 1):
        arr[i] = carr[i - 1] * carr[i + 1]

    arr[0] = carr[0] * carr[1]
    arr[-1] = carr[-2] * carr[-1]


def updateWithoutCopy(arr):  # time: O(n)   space: O(1)
    if len(arr) < 2: return

    last = arr[0]

    for i in range(len(arr) - 1):
        arr[i], last = last * arr[i + 1], arr[i]

    arr[-1] = arr[-1] * last


arr = [2, 3, 4, 5, 6]

updateWithoutCopy(arr)
# 6, 8, 15, 24, 30

print(arr)
