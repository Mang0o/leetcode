"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m<=0 or n<=0:
            return 1
        dp=[1 for _ in range(n)]
        for i in range(1,m):
            for j in range(n):
                dp[j] = 1 if j==0 else dp[j-1]+dp[j]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    m = 3
    n = 7
    print(s.uniquePaths(m,n))