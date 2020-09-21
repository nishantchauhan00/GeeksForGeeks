# A simple solution is to one by one consider all bars as starting points and 
# calculate area of all rectangles starting with every bar. Finally return 
# maximum of all possible areas. Time complexity of this solution would be 
# O(n^2).
def solver1(arr, rows):
    max_area = 0
    for i in range(rows):
        minheight = arr[i]
        for j in range(i, rows):
            minheight = min(minheight, arr[j])
            max_area = max(max_area, minheight * (j - i + 1))

    return max_area


def solver(arr, rows):
    max_area = 0
    return max_area


T = int(input())

for _ in range(T):
    rows = int(input())
    arr = list(map(int, input().split()))
    print(solver(arr, rows))


