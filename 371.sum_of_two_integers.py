class Solution:
    def _getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        s = a ^ b
        carry = (a & b)<<1

        while carry != 0:
            a = s
            b = carry
            s = a ^ b
            carry = (a & b)<<1
        return s

    def _getSub(self,bigger,smaller):
        result = smaller
        ret = 0
        while smaller < bigger:
            smaller = self._getSum(smaller,1)
            ret = self._getSum(ret,1)
        return ret

    def getSum(self,a,b):
        if a >= 0 and b >= 0:
            return self._getSum(a,b)
        if a < 0 and b < 0:
            return self._getSum(~self._getSum(self._getSum(~a,1),self._getSum(~b,1)),1)

        if a < 0:
            a,b = b,a

        b = self._getSum(~b,1)

        if b <= a:
            return self._getSub(a,b)
        else:
            return self._getSum(~self._getSub(b,a),1)

if __name__ == '__main__':
    s = Solution()

    print(s.getSum(-1,1))
    