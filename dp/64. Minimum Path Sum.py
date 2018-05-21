"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]
Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.
"""
class Solution:
    #O(m*n)space
    def minPathSum1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        row,col = len(grid),len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if i == 0:
                    dp[0][j] = grid[0][0] if j==0 else dp[0][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][0] = grid[0][0] if i==0 else dp[i-1][0] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j]) + grid[i][j]

        return dp[row-1][col-1]

    #O(col)space
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        row,col = len(grid),len(grid[0])
        dp = [0 for _ in range(col)]
        dp[0] = grid[0][0]

        for i in range(1,col):
            dp[i] = dp[i-1] + grid[0][i]

        for i in range(1,row):
            for j in range(0,col):
                dp[j] = dp[j] + grid[i][j] if j==0 else min(dp[j-1],dp[j])+grid[i][j]
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    grid = [[1,3,1],
 [1,5,1],
 [4,2,1]]
    print(s.minPathSum(grid))
