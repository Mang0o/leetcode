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
        if not nums: return -1
        index = self.search_rotated_index(nums)
        l = self.binary_search(nums,0,index-1,target)
        if l != -1:
            return l
        r = self.binary_search(nums,index,len(nums)-1,target)
        if r != -1:
            return r
        return -1

    def binary_search(self,nums,left,right,target):
        if nums[left] > target or nums[right] < target:
            return -1
        while left<right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid+1
            else:
                return mid
        return left if nums[left]==target else -1

    def search_rotated_index(self,nums):
        if not nums: return -1
        if len(nums) == 1:return 0
        if len(nums) == 2:return [0,1][nums[1] < nums[0]]
        left,right = 0,len(nums)-1
        while (left<right):
            if left == right - 1:
                return left if nums[left] <= nums[right] else right
            mid = (left+right)//2
            if nums[left] < nums[right]:
                return left
            else:
                if nums[left] > nums[mid]:
                    right = mid
                elif nums[right] < nums[mid]:
                    left = mid
                else:#nums[left] == nums[mid] == nums[right]
                    while (left<mid):
                        if nums[left]==nums[mid]:
                            left+=1
                        elif nums[left] < nums[mid]:
                            return left
                        else:
                            right = mid
                            break
               
        return left if nums[left] <= nums[right] else right

if __name__ == '__main__':
    s = Solution()
    nums = [4,5,6,7,8,0,1,2]
    nums = [4,4,4,4,4,4,4,4]
    print(s.search(nums,4))