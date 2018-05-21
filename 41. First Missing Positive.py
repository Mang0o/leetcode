"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

"""

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 1
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = 0

        for i in range(len(nums)):
            value = nums[i]
            while value <= len(nums) and value > 0:
                tmp = nums[value-1]
                nums[value-1] = -value
                value = tmp
            
        for index,value in enumerate(nums):
            if value >= 0:
                return index+1

        return len(nums)+1





        
        

if __name__ == '__main__':
    s = Solution()
    nums = [-1,3,-1,1,2,5]
    print(s.firstMissingPositive(nums))