"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [False]*len(s)
        ret = [[] for i in range(len(s))]
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp[i] = True
                ret[i].append(s[:i+1])
            for j in range(i):
                if s[j+1:i+1] in wordDict and dp[j]:
                    dp[i] = True
                    ret[i].extend([x+' '+s[j+1:i+1] for x in ret[j]])
        # print(dp)
        # print(ret)
        return ret[-1]
        # return dp[len(s)-1]

if __name__ == '__main__':
    ss = Solution()
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    # s = "catsanddog"
    # wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(ss.wordBreak(s,wordDict))