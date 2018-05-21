"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle."""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp = [nums[0]]

        # for i in range(1,len(nums)):
        #     dp.append(nums[i]+dp[i-1] if nums[i]+dp[i-1]>nums[i] else nums[i])
        # return max(dp)


        if not nums:
            return None
        ret = cur = nums[0]
        for i in nums[1:]:
            cur = cur+i if cur+i > i else i
            ret = max(ret,cur)
        return ret

if __name__ == '__main__':
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))