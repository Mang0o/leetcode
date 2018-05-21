import math
import time
class Solution:
    def wiggleSort1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        print(nums)
        print('=========')
        for i in range(len(nums)-1,0,-1):
            if nums[i] < nums[i-1]:
                nums[i],nums[i-1] = nums[i-1],nums[i]
        print(nums)
        
        
        index = self.helper(nums)
        while index < len(nums) - 1:
            time.sleep(1)
            print(nums,index)
            nums[0],nums[1] = nums[1],nums[0]
            # if nums[0] != nums[index]:
            #     nums[0],nums[index] = nums[index],nums[0]
            # elif index < len(nums) - 1 and (nums[0] != nums[index+1]):
            #     nums[0],nums[index+1] = nums[index+1],nums[0]
            # elif index > 1 and (nums[0]!=nums[index+1]):
            #     nums[0],nums[index+1] = nums[index+1],nums[0]
            # else:
            #     print('wuwuwuw')
            #     break
            index = self.helper(nums)
        
        print(nums)

    def helper(self,nums):
        index = 0
        Flag = True
        for i in range(1,len(nums)):
            # print(index)
            if i == index:
                continue
            if index == len(nums) - 1:
                break

            if nums[i] > nums[index] and Flag:
                if i == index + 1:
                    index += 1
                    Flag = False
                else:
                    nums[i],nums[index+1] = nums[index+1],nums[i]
                    index += 2
            elif nums[i] < nums[index] and (not Flag):
                if i == index + 1:
                    index += 1
                    Flag = True
                else:
                    nums[i],nums[index+1] = nums[index+1],nums[i]
                    index += 2
            else:
                continue
        if index == len(nums) - 2 and ((Flag and nums[-1] > nums[index]) or ((not Flag) and nums[-1] < nums[index])):
            print("gagagagagaga")
            index += 1
        print(index)
        return index

    def wiggleSort(self,nums):
        # tmp = sorted(nums)
        nums.sort()

        print(nums)
        
        tmp = []

        index = math.ceil(len(nums)/2)
        for i in range(index):
            tmp.append(nums[i])
            if (i+index) < len(nums):
                tmp.append(nums[i+index])
            # if i % 2 == 1 and index < len(nums):
            #     nums[i],nums[index] = nums[index],nums[i]
            #     index+=1

        print(tmp)
        nums[:] = tmp
        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                nums[:] = nums[i+1:]+nums[:i+1]
        print(nums)
        


if __name__ == '__main__':
    s = Solution()
    # s.wiggleSort([1,5,1,1,6,4])

    # s.wiggleSort([1,3,4,4,3,1,4,1,1])

    # s.wiggleSort([1,1,3,2,2,3])
    # s.wiggleSort([4,5,5,6])
    # s.wiggleSort([1,3,2,2,3,1])
    s.wiggleSort([2,3,3,2,2,2,1,1])
    # s.wiggleSort([6,5,5])
