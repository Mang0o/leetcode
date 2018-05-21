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
        
        left = 0
        right = len(nums)-1
            
        if right == left:
            if nums[right] == target:
                return [left,right]
            else:
                return [-1,-1]

        first,last = -1,-1
        
        #find the first
        while (left < right):
            if left == right -1:
                if nums[left] == target:
                    first = left
                elif nums[right] == target:
                    first = right
                break
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid
            else:
                right = mid

        # print(first)

        if first == -1:
            return [-1,-1]

        left = 0
        right = len(nums)-1
        #find the last
        while (left < right):
            print(left,right)
            if left == right -1:
                if nums[right] == target:
                    last = right
                elif nums[left] == target:
                    last = left
                break

            mid = (left+right)//2

            print(mid)
            if nums[mid] > target:
                right = mid
            else:
                left = mid

        return [first,last]

if __name__ == '__main__':
    s = Solution()
    nums = [5, 7, 7,7,7,8, 8, 9,9,9,10]
    nums = [1]
    print(s.searchRange(nums,1))



