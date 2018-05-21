class Solution:
    d = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz',
    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.ret = []
        self.length = len(digits)
        self.helper(digits,0,'')
        return self.ret

    def helper(self,digits,depth,tmp_str):
        if depth<self.length:
            for i in Solution.d[digits[depth]]:
                self.helper(digits,depth+1,tmp_str+i)
        else:
            if tmp_str:
                self.ret.append(tmp_str)

if __name__ == '__main__':
    s = Solution()

    print(s.letterCombinations('23546'))
