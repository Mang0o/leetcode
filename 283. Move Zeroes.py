class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0

        while i < len(nums):
            print(i,j)
            if nums[i] != 0:
                i += 1
                continue
            j = i+1 if j < i else j
            while (j<len(nums)):
                if nums[j] == 0:
                    j += 1
                    continue
                break
            if j == len(nums):
                break
            
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j += 1

        while i < len(nums):
            nums[i] = 0
            i += 1

        # index = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[i], nums[index] = nums[index], nums[i]
        #         index += 1


if __name__ == '__main__':
    s = Solution()

    a = [1,0,3,5,0,0,2,6,0]
    s.moveZeroes(a)
    print(a)
    print('abc')