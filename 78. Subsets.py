class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ret = []

        def backtracing(nums,start,tmp_result):
            self.ret.append(tmp_result.copy())
            for i in range(start,len(nums)):
                tmp_result.append(nums[i])
                backtracing(nums,i+1,tmp_result)
                tmp_result.pop()

        backtracing(list(set(nums)),0,[])
        return self.ret
# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         self.ret = []
#         def subsets_helper(nums,index,tmpList):
#             if index == len(nums):
#                 self.ret.append(tmpList.copy())
#                 return
#             subsets_helper(nums,index+1,tmpList+[nums[index]])
#             subsets_helper(nums,index+1,tmpList+[])
#         subsets_helper(nums,0,list())
#         return self.ret

if __name__ == '__main__':
    s = Solution()
    r = s.subsets([1,2,44,5,6,3])

    print(r)