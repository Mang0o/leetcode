import time
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pos = 0
        ret = ''
        try:
            while(True):
                char = None
                for s in strs:
                    if char is None:
                        char = s[pos]
                    elif s[pos] == char:
                        continue
                    else:
                        raise
                ret = ret+char
                pos += 1
        except Exception as e:
            pass
        finally:
            return ret
        


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(['abc1123123','a','abc12344']))