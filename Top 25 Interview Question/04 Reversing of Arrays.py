class Solution:
    def reverseArray(self, arr):
        n = len(arr)
        for i in range(0, int(n / 2)):
            arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
        return arr


print(Solution().reverseArray([1, 2, 3]))
print(Solution().reverseArray([4, 5, 1, 2]))


