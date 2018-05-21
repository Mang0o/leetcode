class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        d1 = dict()
        for i in A:
            for j in B:
                if (i+j) in d1:
                    d1[i+j] += 1
                else:
                    d1[i+j] = 1

        d2 = dict()
        for i in C:
            for j in D:
                if (i+j) in d2:
                    d2[i+j] += 1
                else:
                    d2[i+j] = 1

        ret = 0
        # print(d1,d2)
        for k,v in d1.items():
            if -k in d2:
                # print(k,v,d2[-k])
                ret += (v*d2[-k])
        return ret

if __name__ == '__main__':
    s = Solution()

    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]


    A = [0]
    B = [0]
    C = [0]
    D = [0]
    print(s.fourSumCount(A,B,C,D))    