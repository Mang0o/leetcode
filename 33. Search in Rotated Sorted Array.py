"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while(left <= right):
            if left == right and nums[left] != target:
                return -1
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            
            if right == left+1:
                return -1

            mid = (left+right)//2
            if nums[mid] == target:
                return mid
          
            if nums[left] > target and nums[right] < target:
                return -1

            if nums[mid] > target and nums[left] < target:
                right = mid
            elif nums[mid] > target and nums[left] > target and nums[mid] > nums[left]:
                left = mid
            elif nums[mid] > target and nums[left] > target and nums[mid] < nums[left]:
                right = mid
            elif nums[mid] < target and nums[right] > target:
                left = mid
            elif nums[mid] < target and nums[right] < target and nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < target and nums[right] < target and nums[mid] < nums[right]:
                right = mid
            else:
                return -1
        return -1

if __name__ == '__main__':
    s = Solution()
    nums = [4,5,6,7,0,1,2]
    print(s.search(nums,0))