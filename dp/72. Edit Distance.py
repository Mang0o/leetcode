"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return self.editDistance(word1,word2,1,1,1)
    
    def editDistance(self,word1,word2,insertCost,replaceCost,delCost):
        row = len(word1)+1
        column = len(word2)+1
        
        dp = [[0]*column for j in range(row)]
        
        for i in range(column):
            dp[0][i] = i*insertCost
        for i in range(row):
            dp[i][0] = i*delCost
        for i in range(1,row):
            for j in range(1,column):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1]+replaceCost
                dp[i][j] = min(dp[i][j],dp[i-1][j]+delCost)
                dp[i][j] = min(dp[i][j],dp[i][j-1]+insertCost)
        return dp[-1][-1]
                
