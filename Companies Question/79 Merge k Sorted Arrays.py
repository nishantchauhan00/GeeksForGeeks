# this question should be done in c++, python takes time for it because of
# large memory allocation
# in c++ we can also use priority queue to do this
# https://www.geeksforgeeks.org/merge-k-sorted-arrays-set-2-different-sized-arrays/

def merge1(numbers):  # 1.06s
    return sorted([el for row in numbers for el in row])


def merge2(numbers):  # naive method, tle
    n = len(numbers)
    out = [None for _ in range(n ** 2)]
    pos = [0 for _ in range(n)]

    for i in range(n ** 2):
        min_el, j = 99999, 0
        for k in range(n):
            if pos[k] == n:
                continue
            else:
                if numbers[k][pos[k]] < min_el:
                    min_el = numbers[k][pos[k]]
                    j = k
        pos[j] += 1
        out[i] = min_el
    return out


def merge(numbers): # merge arrays again and again, tle
    n = len(numbers)
    mergedArray = numbers[0]
    for i in range(1, n):
        j, k, l = 0, 0, 0
        newarr = [None for _ in range(n * i + n)]
        while j < n * i and k < n:
            if mergedArray[j] < numbers[i][k]:
                newarr[l] = mergedArray[j]
                j += 1
            else:
                newarr[l] = numbers[i][k]
                k += 1
            l += 1

        while j < n * i:
            newarr[l] = mergedArray[j]
            j += 1
            l += 1
        while k < n:
            newarr[l] = numbers[i][k]
            k += 1
            l += 1
        mergedArray = newarr

    return mergedArray


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        numbers = [[0 for _ in range(n)] for _ in range(n)]
        line = input().strip().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j] = int(line[i * n + j])
        merged_list = merge(numbers)
        for i in merged_list:
            print(i, end=" ")
        print()
