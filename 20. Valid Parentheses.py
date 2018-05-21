class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        m = {
            '(':0,')':1,
            '[':2,']':3,
            '{':4,'}':5,
        }
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if m[i] % 2 == 0:
                    stack.append(i)
                else:
                    tmp = stack[-1]
                    if m[tmp] // 2 == m[i] // 2:
                        stack.pop()
                    else:
                        return False 
        if stack:
            return False
        return True

        

if __name__ == '__main__':
    s = Solution()
    print(s.isValid('([(]))'))
