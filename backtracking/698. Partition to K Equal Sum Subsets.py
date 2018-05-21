"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""

class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < k:
            return False
        if sum(nums)%k!=0:
            return False

        sumk = sum(nums)/k
        length = len(nums)
        visit = [0]*len(nums)

        def dfs(k,nums,startIndex,count,currentSum):
            if k==1:
                return True
            if currentSum==sumk and count>0:
                return dfs(k-1,nums,0,0,0)
            for i in range(startIndex,length):
                if not visit[i] and currentSum+nums[i]<=sumk:
                    visit[i] = True
                    if dfs(k,nums,i+1,count+1,currentSum+nums[i]):
                        return True
                    visit[i] = False
            return False

        return dfs(k,nums,0,0,0)
        
if __name__ == '__main__':
    s = Solution()
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(s.canPartitionKSubsets(nums,k))