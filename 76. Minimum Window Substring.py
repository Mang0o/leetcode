"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""
import time
class Solution:
    # def minWindow(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: str
    #     """
    #     ret = ['']
    #     self.minWindowHelper(s,t,ret)
    #     return ret[0]

    # def minWindowHelper(self,s,t,ret):
    #     # print(s,t)
    #     if not s:
    #         return
    #     if len(t) == 1 and t in s:
    #         ret[0] = t
    #         return
    #     d = {}
    #     index_list = []
    #     for i,value in enumerate(s):
    #         if value not in d:
    #             d[value] = [i]
    #         else:
    #             d[value].append(i)
    #     # print(d)
    #     visited = set([])
    #     for i in t:
    #         if i not in d or (not d[i]):
    #             return
    #         else:
    #             if i not in visited:
    #                 index_list.extend(d[i])
    #                 visited.add(i)
    #             d[i].pop()
    #     # print(index_list,'111')
    #     index_list = sorted(index_list)
    #     print(index_list,'222',s,t)
    #     # time.sleep(2)
    #     if ret[0] == "" or len(ret[0])>len(s):
    #         ret[0] = s
    #     if index_list:
    #         tmp = index_list[0] if index_list[0] > 0 else 1
    #         print('left',tmp)
    #         self.minWindowHelper(s[tmp:],t,ret)
    #         tmp = index_list[-1]+1 if index_list[-1] < len(s)-2 else -1
    #         print('right',tmp)
    #         self.minWindowHelper(s[:tmp],t,ret)

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        self.ret = ''
        d = {}
        count = 0
        i = j = 0
        length = len(s)
        for k in t:
            if k in d:
                d[k] += 1
            else:
                d[k] = 1
                count+=1

        while(j<length):
            if s[j] in d:
                d[s[j]] -= 1
                if d[s[j]] == 0:
                    count -= 1
                if count == 0:
                    while i<j:
                        if s[i] in d:
                            if d[s[i]] < 0:
                                d[s[i]] += 1
                                i+=1
                            else:
                                break
                        else:
                            i+=1
                    if self.ret== "" or len(self.ret) > j-i+1:
                        self.ret = s[i:j+1]
            
            j+=1
        return self.ret


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ret = ""
        max_length = 0
        from collections import Counter
        counter = Counter(t)
        count = len(counter)
        
        left = right = 0
        while(right < len(s)):
            if s[right] in counter:
                counter[s[right]]-=1
                if counter[s[right]] == 0:
                    count-=1
                if count == 0:#左边缩，当左边缩完count会增加的时候，记录一个可行解
                    while(left<=right and count==0):
                        if s[left] in counter:
                            if counter[s[left]]==0:
                                ret = s[left:right+1] if (right-left+1) < len(ret) or ret == '' else ret
                                count+=1
                            counter[s[left]]+=1
                        left+=1
            right+=1
        return ret


if __name__ == '__main__':
    s = Solution()
    # ss = "aaba"
    # t = "aab"
    # ss = 'ask_not_what_your_country_can_do_for_you_ask_what_you_can_do_for_your_country'
    # t = 'ask_country'
    ss = 'aa'
    t = 'aa'
    print(s.minWindow(ss,t),'====')
