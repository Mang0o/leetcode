class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ret = []
        if n == 0:
            return ret
        self.addParenthesis(1,2*n,ret,'',0,0)
        return ret

    def addParenthesis(self,depth,n,ret,str,lnum,rnum):
        if lnum < rnum or lnum > n/2:
            return

        if depth == n:
            ret.append(str+')')
            return
        else:
            self.addParenthesis(depth+1,n,ret,str+'(',lnum+1,rnum)
            self.addParenthesis(depth+1,n,ret,str+')',lnum,rnum+1)

if __name__ == '__main__':
    s = Solution()

    print(s.generateParenthesis(4))
