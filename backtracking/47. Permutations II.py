"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ret = []
        self.length = len(nums)
        self.ret_set = set([])
        def helper(nums,visited,depth,tmpList):
            if depth == self.length:
                if tuple(tmpList) not in self.ret_set:
                    self.ret.append(tmpList.copy())
                    self.ret_set.add(tuple(tmpList))
                return
            
            for i in range(self.length):
                if not visited[i]:
                    visited[i] = True
                    tmpList.append(nums[i])
                    helper(nums,visited,depth+1,tmpList)
                    tmpList.pop()
                    visited[i] = False
            return
        visited = [False for i in nums]
        helper(nums,visited,0,list())

        return self.ret

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2]
    print(s.permuteUnique(nums))
    