"""
Input: 23, 34, 56, 21, 21, 56, 78, 23, 34
Output: 23
Hint: USE XOR
"""


def uniqueval(arr):
    out = arr[0]
    for i in range(1, len(arr)):
        out ^= arr[i]

    return out


print(uniqueval([23, 34, 56, 21, 21, 56, 78, 23, 34]))
