#
#    RECURSION - BAD WAY, gives tle
#
def is_k_palin1(inp, k):
    def isPalindrome(s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def helper(curr, k_curr, i, n):
        if isPalindrome(curr):
            return True
        if k_curr == k or i == n:
            return False

        considered = helper(curr, k_curr, i + 1, n)
        not_considered = helper(curr[:i] + curr[i + 1 :], k_curr + 1, i + 1, n)
        return considered or not_considered

    return 1 if helper(inp, 0, 0, len(inp)) else 0


#
#    RECURSION - BETTER WAY, but still gives tle
#
def is_k_palin2(inp, k):
    def helper(curr, k_curr):
        print(curr, k_curr)
        if len(curr) <= 1:
            return True

        i, j = 0, len(curr) - 1
        while curr[i] == curr[j]:
            i += 1
            j -= 1
            if j - i < 1:
                return True

        curr = curr[i : j + 1]
        if k_curr == 0:
            return False

        return helper(curr[1:], k_curr - 1) or helper(curr[:-1], k_curr - 1)

    return 1 if helper(inp, k) else 0


#
#    using longest common subsequence
#
'''
This problem can be solved using the famous Longest Common Subsequence(LCS) 
method. When LCS is applied with the string and the reverse of the given string, 
then it gives us the longest palindromic subsequence present in the string.

Let the longest palindromic subsequence length of a given string of length 
string_length be palin_length. Then (string_length - palin_length) gives the 
number of characters required to be deleted to convert the string to a 
palindrome. 
Thus, the given string is k-palindrome if (string_length - palin_length) <= k.

Let me give some examples,
Initial String: madtam (string_length = 6)
Longest Palindromic Subsequence: madam (palin_length = 5)
Number of non-contributing characters: 1 ( string_length - palin_length)
Thus this string is k-palindromic where k>=1. This is because you need to 
delete atmost k characters ( k or less).
'''
def is_k_palin(inp, k):
    def lcs(str1, str2, m, n):  # dp
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]

    lcs_inp = lcs(inp, inp[::-1], len(inp), len(inp))

    return 1 if (len(inp) - lcs_inp <= k) else 0



T = int(input())

for _ in range(T):
    inp, k = input().split()
    print(is_k_palin(inp, int(k)))
