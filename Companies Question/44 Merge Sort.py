def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) / 2
        
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# The first Array is : arr[l...m]
# The Second Array is : arr[m+1...r]
def merge(arr, l, m, r):
    temp = [None for _ in range(r - l + 1)]
    i = l
    j = m + 1
    k = 0

    while i <= m and j <= r:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= m:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= r:
        temp[k] = arr[j]
        j += 1
        k += 1

    i = 0
    while l <= r:
        arr[l] = temp[i]
        i += 1
        l += 1
