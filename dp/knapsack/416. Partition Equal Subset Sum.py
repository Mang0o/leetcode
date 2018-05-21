"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""

class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        s = sum(nums)
        if s%2==1: return False
        half = s//2
        dp = []
        for i in range(len(nums)+1):
            dp.append([False for i in range(half+1)])
        
        for j in range(half+1):
            dp[0][j] = False
        for i in range(len(nums)+1):
            dp[i][0] = True
        dp[0][0] = True

        for i in range(1,len(nums)+1):
            for j in range(1,half+1):
                dp[i][j] = dp[i-1][j]
                if j-nums[i-1]>=0:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
        return dp[len(nums)][half]

    def canPartitionV2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        s = sum(nums)
        if s%2==1: return False
        half = s//2
        dp = [True]
        for j in range(1,half+1):
            dp.append(False)

        for i in range(1,len(nums)+1):
            print(dp)
            for j in range(half,0,-1):
                if j-nums[i-1]>=0:
                    dp[j] = dp[j-nums[i-1]] or dp[j]
        return dp[half]

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    print(s.canPartitionV2(nums))

    print(sum([4, 3, 2, 3, 5, 2, 1]))

