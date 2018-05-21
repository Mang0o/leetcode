class Solution:

    def myAtoi(self,str):
        ret = self._myAtoi(str)

        if ret > 2**31-1:
            ret = 2**31-1
        if ret < -2**31:
            ret = -2**31

        return ret


    def _myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        

        str = str.strip()

        index = -1
        for i in str:
            index += 1
            if i not in '0123456789+-':
                str = str[:index]
        if str == '' or len(str) == 0:
            return 0
        if str[0] == '-' or str[0] == '+':
            if len(str) <= 1:
                return 0

            for i in str[1:]:
                if i not in '0123456789':
                    return 0

            flag = -1 if str[0] == '-' else 1

            return flag*self.helper(str[1:])

        return self.helper(str)

    def helper(self,str):
        bits = 0
        ret = 0
        for i in range(len(str),0,-1):
            ret += (ord(str[i-1]) - ord('0'))*(10**bits)
            bits+= 1
        return ret





def main():
    s = Solution()
    ss = "abc"

    print(s.myAtoi(ss))

if __name__ == '__main__':
    main()