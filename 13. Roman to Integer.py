class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d = {'M':1000,'D':500,'C':100,'L':50,'X':10,"V":5,'I':1}

        ret = 0
        pos = 0
        while(pos < len(s)):
            if pos == len(s) -1:
                ret += d[s[pos]]
                break
            if d[s[pos]] == d[s[pos+1]]:
                ret+= d[s[pos]]
                pos+=1
            elif d[s[pos]] < d[s[pos+1]]:
                ret += (d[s[pos+1]] - d[s[pos]])
                pos+=2
            else:
                ret += d[s[pos]]
                pos+=1
        return ret

if __name__ == '__main__':
    print(Solution().romanToInt('MCMXCVI'))


