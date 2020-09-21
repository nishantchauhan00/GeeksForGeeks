from functools import reduce


class Solution:
    def maxthreemul1(self, arr, n=3):  # brute force
        maxmul = -99999
        # a, b, c = -1, -1, -1
        for i in range(0, len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    maxmul = max(maxmul, arr[i] * arr[j] * arr[k])
                    # #         OR
                    # if maxmul < arr[i] * arr[j] * arr[k]:
                    #     maxmul = arr[i] * arr[j] * arr[k]
                    #     a, b, c = i, j, k
        # print(a, b, c)
        return maxmul

    def maxthreemul2(self, arr, n=3):  # works only for positive values array
        if len(arr) < 3:
            return -9999

        vals = [arr[0], arr[1], arr[2]].copy()

        def minhelp(vals):
            if vals[0] < vals[1]:
                return 0 if vals[0] < vals[2] else 2
            else:
                return 1 if vals[1] < vals[2] else 2

        for i in range(3, len(arr)):
            mindex = minhelp(vals)
            if arr[i] > vals[mindex]:
                vals[mindex] = arr[i]
        return reduce(lambda x, y: x * y, vals)

    def maxthreemul3(self, arr, n=3):  # using sorting
        if len(arr) < 3:
            return -9999

        arr.sort()
        return max(arr[0] * arr[1] * arr[-1], arr[-3] * arr[-2] * arr[-1])

    def maxthreemul4(self, arr, n=3):
        arrlen = len(arr)
        if arrlen < 3:
            return -9999

        # we are taking min values too beacuse of negative values
        leftmax, leftmin, rightmax, rightmin = (
            [-1] * arrlen,
            [-1] * arrlen,
            [-1] * arrlen,
            [-1] * arrlen,
        )

        lmax, lmin = arr[0], arr[0]
        for i in range(1, arrlen):
            leftmax[i] = lmax
            if arr[i] > lmax:
                lmax = arr[i]

            leftmin[i] = lmin
            if arr[i] < lmin:
                lmin = arr[i]

        rmax, rmin = arr[-1], arr[-1]
        for i in range(arrlen - 2, -1, -1):
            rightmax[i] = rmax
            if arr[i] > rmax:
                rmax = arr[i]

            rightmin[i] = rmin
            if arr[i] < rmin:
                rmin = arr[i]

        # For all array indexes i except first and
        # last, compute maximum of arr[i]*x*y where
        # x can be leftMax[i] or leftMin[i] and
        # y can be rightMax[i] or rightMin[i].
        maxprod = arr[0] * arr[1] * arr[2]
        for i in range(1, arrlen - 1):
            maxprod = max(
                maxprod,
                arr[i] * leftmax[i] * rightmax[i],
                arr[i] * leftmin[i] * rightmin[i],
                arr[i] * leftmax[i] * rightmin[i],
                arr[i] * leftmin[i] * rightmax[i],
            )

        return maxprod

    def maxthreemul(self, arr, n=3):
        arrlen = len(arr)
        if arrlen < 3:
            return -9999
        # 1. Scan the array and compute Maximum, second maximum and third maximum
        #     element present in the array.
        # 2. Scan the array and compute Minimum and second minimum element present
        #      in the array.
        # 3. Return the maximum of product of Maximum, second maximum and third
        #     maximum and product of Minimum, second minimum and Maximum element.

        # three maximum elements
        valsmax = [arr[0], arr[1], arr[2]].copy()

        def minhelp(valsmax):  # returns index of minimum element of three max
            if valsmax[0] < valsmax[1]:
                return 0 if valsmax[0] < valsmax[2] else 2
            else:
                return 1 if valsmax[1] < valsmax[2] else 2

        minindex = minhelp(valsmax)
        for i in range(3, len(arr)):
            if arr[i] > valsmax[minindex]:
                valsmax[minindex] = arr[i]
                minindex = minhelp(valsmax)

        # two minimum elements
        valsmin = [arr[0], arr[1]].copy()

        def maxhelp(valsmin):
            return 0 if valsmin[0] > valsmin[1] else 1

        maxindex = maxhelp(valsmin)
        for i in range(2, len(arr)):
            if arr[i] < valsmin[maxindex]:
                valsmin[maxindex] = arr[i]
                maxindex = maxhelp(valsmin)

        return max(
            valsmax[0] * valsmax[1] * valsmax[2], valsmin[0] * valsmin[1] * max(valsmax)
        )


print(Solution().maxthreemul([]))
print(Solution().maxthreemul([1, 2, 3]))
print(Solution().maxthreemul([7, 4, 4, 1, 5]))
print(Solution().maxthreemul([-4, 3, 1, -5, 2]))
print(Solution().maxthreemul([10, 3, 5, 6, 20]))
print(Solution().maxthreemul([-10, -3, -5, -6, -20]))
print(Solution().maxthreemul([1, -4, 3, -6, 7, 0]))
