def solver(arr, n):
    inv_count = 0
    def MergeSort(arr, start, end):
        nonlocal inv_count
        mid = int((start + end) / 2)

        if start < end:
            MergeSort(arr, start, mid)
            MergeSort(arr, mid + 1, end)

        temp = []

        a1 = start
        a2 = mid + 1
        i = start
        while a1 <= mid and a2 <= end:
            if arr[a1] <= arr[a2]:
                temp.append(arr[a1])
                i += 1
                a1 += 1
            else:
                # we can also do (mid-a1+1), but for clear code, i took a
                # different index
                inv_count += mid - i + 1
                temp.append(arr[a2])
                a2 += 1

        while a1 <= mid:
            temp.append(arr[a1])
            a1 += 1

        while a2 <= end:
            temp.append(arr[a2])
            a2 += 1

        i = 0
        while start <= end:
            arr[start] = temp[i]
            start += 1
            i += 1
        
    MergeSort(arr, 0, n-1)

    return inv_count




if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solver(arr, n))