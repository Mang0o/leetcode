class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return -1
        char_dict = {}
        l = len(s)+1
        index = 0
        for i in s:
            if i not in char_dict:
                char_dict[i] = index
            else:
                char_dict[i] = l
            index += 1
        ret = min(char_dict.values())
        print(char_dict.values())
        
        if ret == l:
            ret = -1

        return ret

if __name__ == '__main__':
    s = Solution()

    print(s.firstUniqChar('cc'))