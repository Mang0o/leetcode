"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
"""

class Solution:
    # def maxCoins(self, nums):  
    #     tmpNums = []
    #     for i in nums:
    #         if i > 0:
    #             tmpNums.append(i)

    #     def burst(nums):
    #         ret = 0
    #         num = 1
    #         for i in range(len(nums)):
    #             left = 1 if i==0 else burst(nums[:i])
    #             right = 1 if i==len(nums)-1 else burst(nums[i+1:])
    #             if nums[i]*left*right > ret:
    #                 num = nums[i]
    #                 ret = nums[i]*left*right
    #         print(ret)
    #         return num
    #     burst(nums)
    #     return self.ret

    #dp
    def maxCoins(self, iNums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [i for i in iNums if i > 0] + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        for k in range(2, n):
            for left in range(0, n - k):
                right = left + k
                for i in range(left + 1,right):
                    dp[left][right] = max(dp[left][right],
                           nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)
        memo = [[0]*n for _ in range(n)]


        def burst(memo,nums,left,right):
            if memo[left][right] > 0:
                return memo[left][right]
            ret = 0
            for i in range(left+1,right):
                ret = max(ret, nums[left]*nums[i]*nums[right]\
                    +burst(memo,nums,left,i) + burst(memo,nums,i,right)
                    )
            memo[left][right] = ret
            return ret
        return burst(memo,nums,0,n-1)

if __name__ == '__main__':
    s = Solution()
    # nums = [2,4,8,4,0,7,8,9,1,2,4,7,1,7,3]
    nums = [3]
    print(s.maxCoins(nums))


