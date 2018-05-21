"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ret = 0
        sign = True if (dividend>0 and divisor>0) or (dividend<0 and divisor<0) else False
        if dividend == 0:
            return 0
        dividend = max(dividend,0-dividend)
        divisor = max(divisor,0-divisor)
        
        if dividend < divisor:
            return 0
        
        ret = 0
        while(divisor <= dividend):
            print(divisor,dividend)
            r = 1
            tmp = divisor
            remiain = 0
            while(tmp < dividend):
                remiain = dividend-tmp
                tmp += tmp
                if tmp < dividend:
                    r += r
                # tmp += tmp
            ret += r
            dividend = remiain
            
        
        
        
        if not sign:
            ret = 0 - ret
        ret = min(ret,2147483647)
        ret = max(ret,-2147483648)
        return ret
            

if __name__ == '__main__':
    s = Solution()

    print(s.divide(-2,-1))