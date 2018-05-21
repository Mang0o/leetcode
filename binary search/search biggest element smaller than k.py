"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
class Solution:
    def searchIndex(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if (not nums) or nums[0]>=target:
            return -1
        if nums[-1]<target:return len(nums)-1
        left,right = 0,len(nums)-1
        while(left<right):
            mid = (left+right)//2
            if nums[mid]<target:
                left= mid+1
            elif nums[mid]>= target:
                right = mid-1

        if nums[left]>=target:
            return left-1
        else:
            return left

if __name__ == '__main__':
    s = Solution()
    nums = [3,5, 6,6,7, 7,7,7,8, 8, 9,9,9,10]
    nums = [3]
    # nums = [1]
    # nums = []
    print(s.searchIndex(nums,4))

    print(list(enumerate(nums)))

    
    print('z'<'b')



