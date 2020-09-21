def solver1(arr, n, k):  # the bad solution
    return sorted(arr)[k - 1]


# although its a good solution, but it is giving tle, :|
def solver(arr, n, k):  # the good solution, modified quick sort
    def partition(low, high):
        i = low - 1  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):
            if arr[j] < pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1 # correct position of pivot

    def quickSort(low, high):
        # although in sorting we just use '<' sign, but here we use '<=', 
        # because element might be in low/high but not able to return because 
        # low == high, && we are also not passing k and arr here, because, they are
        # local functions so its available to them
        if low <= high:
            if low == high:
                return arr[low]
            pivot = partition(low, high)
            if pivot == k - 1:
                return arr[k - 1]
            elif pivot > k - 1:
                return quickSort(low, pivot - 1)
            else:  # pivot < k
                return quickSort(pivot + 1, high)

    return quickSort(0, n - 1)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        k = int(input())
        print(solver(arr, n, k))

        