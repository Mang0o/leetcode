import time
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        v = [True]
        for i in range(len(s)+1):
            v.append(False)

        wd = set(wordDict)
        for i in range(0,len(s)):
            print(i,s[:i+1])
            if s[:i+1] in wd:
                v[i+1] = True
                continue
            
            for j in range(0,i+1):
                print(i,j,s[j+1:i+1])
                if s[j+1:i+1] in wd and v[j+1]:
                    v[i+1]=True
                    break
        print(v)
        return v[len(s)]



if __name__ == '__main__':
    s = Solution()
    # ss = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
    # ss = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    ss = 'leetcode'
    # wd = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    # wd = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    wd = ['leet','code']
    print(s.wordBreak(ss,wd))