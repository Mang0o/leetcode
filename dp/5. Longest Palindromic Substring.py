class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        
        max_length = 0
        start = end = 0
        
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if j-i<=1:
                    if s[i]==s[j]:
                        dp[i][j] = True
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                
                if dp[i][j] and j-i+1>max_length:
                    max_length = j-i+1
                    start = i
                    end = j
                    
        return s[start:end+1]