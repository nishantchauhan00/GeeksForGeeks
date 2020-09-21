'''
https://youtu.be/3hNuefaICxw

https://www.youtube.com/watch?v=AVQednPx5t8&feature=youtu.be&ab_channel=CodingDoor

F(i, j)  represents the maximum value the user can collect from 
         i'th coin to j'th coin.

    F(i, j)  = Max(Vi + min(F(i+2, j), F(i+1, j-1) ), 
                   Vj + min(F(i+1, j-1), F(i, j-2) )) 

Base Cases
    F(i, j)  = Vi           If j == i
    F(i, j)  = max(Vi, Vj)  If j == i+1
'''
def solver(arr, n):
    dp = [[-1 for _ in range(n)]for _ in range(n)]

    def helper(i, j):
        if i == j: # 1 element left
            return arr[i]
        if i+1 == j: # only two elements left
            return max(arr[i], arr[j])

        if dp[i][j] != -1:
            return dp[i][j]

        # we are using minimum of next moves, because our opponent is as smart
        # as us, so he will make try to make maximum score too, which means 
        # minimum next score for us
        # therefore we have to take current max choice and expect minimum future
        # results

        # 'A' will pickup either first or last
        # 'A' pick first coin
        #             min(  B pick first  ,       B picks last )
        v1 = arr[i] + min(helper(i + 2, j), helper(i + 1, j - 1))
        # 'A' pick last coin
        v2 = arr[j] + min(helper(i + 1, j - 1), helper(i, j - 2))
        dp[i][j] = max(v1, v2)

        return dp[i][j]

    return helper(0, n - 1)




for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solver(arr, n))
