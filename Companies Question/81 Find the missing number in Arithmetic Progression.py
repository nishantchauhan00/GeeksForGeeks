"""
one thing for sure, first element cant go missing, because if it goes missing
then next element will be considered first, so missing element will never be
found, 
> same applies for last element of array

> so as one element is missing, total elemnts = n+1
> therefore AP difference is (high-low)/n, ((n-1) + 1) = n
Ex- [2, 4], diff = (4-2)/(2-1)  
Ex- [2, 4, 6], diff = (6-2)/(3-1)  


one method is go for linear search, but that would give tle
other method is to do binary search
"""


def findMissingUtil(arr, low, high, diff):
    if low >= high:
        return None

    mid = int(low + (high - low) / 2)

    # The element just after mid is missing
    if arr[mid + 1] - arr[mid] != diff:
        return arr[mid] + diff

    # The element just before mid is missing
    if mid > 0 and arr[mid] - arr[mid - 1] != diff:
        return arr[mid - 1] + diff

    # If the elements till mid follow AP, then recur for right half
    if arr[mid] == arr[0] + mid * diff:
        return findMissingUtil(arr, mid + 1, high, diff)
    else:  # Else recur for left half
        return findMissingUtil(arr, low, mid - 1, diff)


def findMissing(arr, n):
    diff = (arr[n - 1] - arr[0]) / n
    return findMissingUtil(arr, arr[0], arr[n - 1], diff)


arr = [2, 4, 8, 10, 12, 14]
n = len(arr)
print("The missing element is", findMissing(arr, n))
