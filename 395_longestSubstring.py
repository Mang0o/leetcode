from collections import Counter
class Solution:
    #version 1
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s == '' or len(s) == 0 or k>len(s):
            return 0
        if k <= 1:
            return len(s)

        pos_dict = {}

        index = 0
        for i in s:
            if i not in pos_dict:
                pos_dict[i] = [index]
            else:
                pos_dict[i].append(index)
            index += 1

        split_point = []
        for _,v in pos_dict.items():
            if len(v) < k:
                split_point += v
        
        if len(split_point) == 0:
            return len(s)

        if len(split_point) == len(s):
            return 0

        new_s = ''
        for i in range(len(s)):
            if i not in split_point:
                new_s += s[i]
            else:
                new_s += ' '

        max_length = 0
        for i in new_s.split():
            max_length = max(max_length,self.longestSubstring(i,k))

        return max_length
    
    #version 2
    def longestSubstring_v2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s == '' or len(s) == 0 or k>len(s):
            return 0
        if k <= 1:
            return len(s)

        del_char = set()
        for i,v in Counter(s).items():
            if v < k:
                del_char.add(i)
        
        if len(del_char) == 0:
            return len(s)
        
        ##不支持含空格,特别追求完美的，可以记下pos，然后用下面的process_string
        new_s = ''.join([i if i not in del_char else ' ' for i in s])

        max_length = 0
        for i in new_s.split():
            max_length = max(max_length,self.longestSubstring_v2(i,k))

        return max_length

    def process_string(self,string, pos):
        result = []
        before = 0
        pos = set(pos)
        for i in range(len(string) + 1):
            if (i in pos) or (i == len(string)):
                current = string[before:i]
                if current:
                    result.append(current)
                before = i + 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.longestSubstring_v2('aaabb',3))

    # print(s.process_string('aaabb',[3,4]))


