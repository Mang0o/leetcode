"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

class Solution:
    def longestValidParentheses1(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = [0,0]
        for i in range(1,len(s)):
            if s[i-1:i+1] == "()":
                dp.append(dp[i-1] + 2)
            elif s[i-1:i+1] == "))" and i-dp[i]-1>=0 and s[i-dp[i]-1] == "(":
                dp.append(dp[i] + 2 + dp[i-dp[i]-1])
            else:
                dp.append(0)
        print(dp)
        return max(dp)

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0,0]
        for i in range(1,len(s)):
            if s[i] == ")":
                if s[i-1] == "(":  #if string looks like ".......()"
                    dp.append(dp[-2] + 2)
                elif s[i-1] == ")" and i-dp[-1]-1>=0 and s[i-1-dp[-1]] == "(":  #string looks like ".......)) and s[i - dp[i - 1] - 1] = '("
                    dp.append(dp[-1] + 2 + dp[-1-dp[-1]-1])
                else:
                    dp.append(0)    
            else:
                dp.append(0)
        print(dp)
        return max(dp)

if __name__ == '__main__':
    s = Solution()
    a = "()(())"
    print(s.longestValidParentheses(a))
