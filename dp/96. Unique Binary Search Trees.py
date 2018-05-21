"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        dp = [0 for i in range(n+1)]
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):  #填表
            for j in range(1,i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(4))