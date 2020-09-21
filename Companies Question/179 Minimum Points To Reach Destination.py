'''
Given a grid of size M*N with each cell consisting of an integer which represents 
points. We can move across a cell only if we have positive points. Whenever we 
pass through a cell, points in that cell are added to our overall points, the 
task is to find minimum initial points to reach cell (m-1, n-1) from (0, 0) by 
following these certain set of rules :
 
1. From a cell (i, j) we can move to (i + 1, j) or (i, j + 1).
2. We cannot move from (i, j) if your overall points at (i, j) are <= 0.
3. We have to reach at (n-1, m-1) with minimum positive points i.e., > 0.


geeksforgeeks.org/minimum-positive-points-to-reach-destination/
'''
import sys

class Solution:
    # brute force - recursion
    def minPoints1(self, arr, M, N):
        vis = [[False for _ in range(N)] for _ in range(M)]
        min_points = sys.maxsize

        def helper(i=0, j=0, points=1, start_points = 1):
            nonlocal min_points
            if i < 0 or j < 0 or i >= M or j >= N or vis[i][j]:
                return

            points += arr[i][j]
            if points <= 0:
                start_points += abs(points) + 1
                points = 1

            if i == M-1 and j == N-1:
                min_points = min(min_points, start_points)
                return
            
            vis[i][j] = True
            helper(i+1, j, points, start_points)
            helper(i, j+1, points, start_points)
            vis[i][j] = False
        
        helper()
        return min_points
		

    ######################
    # DP
    ######################
    '''
    Somethings maybe written clearly though:
    1. We can not use top left to bottom right DP because we cannot guarantee 
       the min points at each cell. Only by using the information from (i+1,j) 
       and (i,j+1) can we decide that. Hence reverse procedure. We assign the 
       min value possible for (m-1,n-1) cell.
    2. dp[i][j] represents the min points needed to continue the journey from 
       (i,j). Firstly it must be atleast 1. Also we may go to (i+1,j) from here 
       or (i,j+1) and we already know the min points needed to reach the end 
       from both of them. So take minimum and we may gain or lose point on 
       (i,j) compensate for that too. Remember minimum points needed to enter 
       may be less but we have a restriction to have atleast 1 point.
    '''
    def minPoints(self, arr, M, N):
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
		
        if arr[M-1][N-1] > 0:
            dp[M-1][N-1] = 1
        else:
            dp[M-1][N-1] = abs(arr[M-1][N-1]) + 1

        # last column and last row
        for i in range(M-2, -1, -1):
            dp[i][N-1] = max(dp[i+1][N-1] - arr[i][N-1], 1)
        for j in range(N-2, -1, -1):
            dp[M-1][j] = max(dp[M-1][j+1] - arr[M-1][j], 1)
        
        for r in range(M-2, -1, -1):
            for c in range(N-2, -1, -1):
                min_points_on_exit = min(dp[r+1][c], dp[r][c+1])
                # it must be at least 1 to contnue journey
                dp[r][c] = max(min_points_on_exit - arr[r][c], 1)

        return dp[0][0]

        
		



# # # # # # # # # # # # # # # # 
# #     DRIVER
# # # # # # # # # # # # # # # # 
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m,n = input().split()
		m,n = int(m),int(n)
		points = []
		for _ in range(m):
			temp = [int(x) for x in input().split()]
			points.append(temp)
		ob = Solution()
		ans = ob.minPoints(points,m,n)
		print(ans)