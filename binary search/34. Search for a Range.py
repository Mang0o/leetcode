"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self.search(nums,0,len(nums)-1,target,-1)
        end = self.search(nums,0,len(nums)-1,target,1)
        return [start,end]

    def search(self,nums,left,right,target,flag):
        if not nums:return -1
        while left<right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else: #nums[mid] == target
                if (mid+flag)>=0 and (mid+flag)<len(nums) and nums[mid+flag] == target:
                    if flag == 1:
                        left = mid+1
                    else:
                        right = mid-1
                else:
                    return mid
        return [-1,left][nums[left]==target] 

if __name__ == '__main__':
    s = Solution()
    nums = [5, 7, 7,7,7,8, 8, 9,9,9,10]
    # nums = [1]
    # nums = []
    # print(s.searchRange(nums,10))

    print(list(enumerate(nums)))



