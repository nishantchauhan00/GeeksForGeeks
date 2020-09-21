import sys

# bruteforce
def solver1(arr, n):
    def helper(i, sum1, sum2):
        if i == n:
            return abs(sum2 - sum1)

        # current arr[i] can only be added with either set
        s1 = helper(i + 1, sum1 + arr[i], sum2)
        s2 = helper(i + 1, sum1, sum2 + arr[i])
        return min(s1, s2)

    return helper(0, 0, 0)


# dp
def solver2(arr, n):
    total = sum(arr)
    # dp[i][j] =
    # (do there exist n-1 number to sum to target j) - exclude arr[n]
    #                            OR
    # (do there exist n-1 number to sum to target (j - arr[n])) - include arr[n]
    dp = [[None for _ in range(total + 1)] for _ in range(n + 1)]

    # for total = 0, no element is needed so it will be TRUE
    for i in range(n + 1):
        dp[i][0] = True

    # for 0 elements the sum cant be greater than 0, so first row except
    # 0th element is false
    for i in range(1, total + 1):
        dp[0][i] = False

    for t in range(1, n + 1):
        for i in range(1, total + 1):
            # if the value while considering current value become negative
            # then just put previous value
            if (i - arr[t - 1]) >= 0:
                dp[t][i] = dp[t - 1][i] or dp[t - 1][i - arr[t - 1]]
            else:
                dp[t][i] = dp[t - 1][i]

    min_diff = sys.maxsize
    for t in range(total + 1):
        if dp[n][t]:
            s1 = t
            s2 = total - t
            min_diff = min(min_diff, abs(s2 - s1))
    return min_diff


'''
Best solution
Most efficient

Tabulation/DP method will iterate through numbers which might not be possible 
to add up from the list.

Consider list [1,9]
In the tabulation method, we will iterate through 0 to 10(1+9), but the only 
possible sums are 0,1,9,10. So the computation for iterating the whole table 
is wasted, instead, we can only calculate the possible sums...

tot=sum(a)
	dp=set() # Initialize a dp set
	dp.add(0) # add zero as empty set always make zero sum
	for element in a: # iterate through all the elements in the list
		new_sums=set() # use this set to store the new set which will be generated from the previously calculated sums
		for i in dp: # iterate through previously calculated sums and add the current elemet
			new_sums.add(i+element)
		dp=dp.union(new_sums) # update the dp with new sums
	minn=float('inf')
	for i in dp:
		minn=min(minn,abs(tot-2*i))
	print(minn)
'''
def solver(arr, n):
    total = sum(arr)
    dp = set()
    dp.add(0) 
    # it helps in saving time by not iterating unpossible sum
    for el in arr:
        new_sum = set()
        for t in dp:
            new_sum.add(t + el)
        dp = dp.union(new_sum)
    
    min_diff = sys.maxsize
    for t in dp:
        s1 = t
        s2 = total - t
        min_diff = min(min_diff, abs(s2-s1))

    return min_diff
    






for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    # print minimum absolute difference
    print(solver(arr, n))
