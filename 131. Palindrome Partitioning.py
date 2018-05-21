"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # dp = [[0]*len(s) for _ in range(len(s))]
        memo,dp = [],[]

        for i in range(len(s)):
            memo.append([])
            dp.append([])
            for j in range(len(s)):
                memo[-1].append([])
                dp[-1].append(0)

        d = {}
        for i in range(len(s)-1,-1,-1):
            for j in range(len(s)-1,i-1,-1):
                    dp[i][j] = (j-i)+1 if s[i] ==  s[j] and (j-i<=1 or dp[i+1][j-1] > 0) else 0
                    if dp[i][j] > 0:
                        if i not in d:
                            d[i] = []
                        d[i].append((i,j))

        def get_result(start,end):
            if start>end:
                return []
            if not memo[start][end]:
                ret = []
                for pair in d[start]:
                    if pair[1]+1 <= end:
                        ret.extend([[s[pair[0]:pair[1]+1]]+i for i in get_result(pair[1]+1,end)])
                    else:
                        ret.append([s[pair[0]:pair[1]+1]])
                memo[start][end] = ret
            return memo[start][end]
        return get_result(0,len(s)-1)

if __name__ == '__main__':
    s = Solution()

    ss = 'aabacab'
    s.partition(ss)