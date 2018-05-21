"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
class Solution:
    def nextPermutation1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        index_i = -1
        length = len(nums)
        for i in range(length - 1):
            if nums[i] < nums[i+1]:
                index_i = i
        if index_i == -1:
            for i in range(length//2):
                nums[i],nums[length-1-i] = nums[length-1-i],nums[i]
        else:
            index_j = -1
            for i in range(index_i,length):
                if nums[i] > nums[index_i]:
                    index_j = i
            nums[index_i],nums[index_j] = nums[index_j],nums[index_i]
            for i in range(0,(length-index_i-1)//2):
                nums[index_i+1+i],nums[length-1-i] = nums[length-1-i],nums[index_i+1+i]

"""
Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, the permutation is sorted in descending order, just reverse it to ascending order and we are done. For example, the next permutation of [3, 2, 1] is [1, 2, 3].
Find the largest index l greater than k such that nums[k] < nums[l].
Swap the value of nums[k] with that of nums[l].
Reverse the sequence from nums[k + 1] up to and including the final element nums[nums.size() - 1]
"""

    def nextPermutation2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(array,start_index=0):
            for i in range((len(array)-start_index+1)//2):
                array[start_index+i],array[-1-i] = array[-1-i],array[start_index+i]

        index_i,index_j,length = -1,-1,len(nums)
        for i in range(length - 1):
            if nums[i] < nums[i+1]:
                index_i = i
        if index_i == -1:
            reverse(nums)
        else:
            for i in range(index_i,length):
                if nums[i] > nums[index_i]:
                    index_j = i
            nums[index_i],nums[index_j] = nums[index_j],nums[index_i]
            reverse(nums,index_i+1)

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(array,start,end):
            for i in range((end-start+1)//2):
                array[start+i],array[end-i]=array[end-i],array[start+i]
        k = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                k = i
                break
        if k == -1:
            reverse(nums,0,len(nums)-1)
        else:
            l = -1
            for j in range(len(nums)-1,k,-1):
                if nums[j] > nums[k]:
                    l = j
                    break
            nums[k],nums[l] = nums[l],nums[k]
            reverse(nums,k+1,len(nums)-1)

if __name__ == '__main__':
    s = Solution()
    a = [1,3,2]
    s.nextPermutation(a)
    print(a)


